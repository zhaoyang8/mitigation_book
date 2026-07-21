#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate markdown tables from the paper tex.

The paper .tex is the single source of truth. For each configured table this
script locates the tex `tabular` by its \\label, converts it to a markdown
table, and writes it to docs/_static/table/<name>.md. The notebooks include
those files with a MyST directive, e.g.

    ```{include} ../_static/table/svrd_rd_decomposition.md
    ```

so the notebooks themselves are never rewritten -- only the generated .md
files change when the tex changes.

Usage:
    python tools/sync_tables_from_tex.py            # (re)write the .md files
    python tools/sync_tables_from_tex.py --check     # report only, exit 1 if stale

Failure is loud: a \\label matching 0 or >1 *live* table environments, or an
out-of-range tabular index, aborts with a non-zero exit and writes nothing, so
a broken parse can never publish bad numbers.
"""
import os
import re
import sys
import difflib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX = os.path.join(REPO, "paper", "mitigation_7-4.tex")
OUTDIR = os.path.join(REPO, "docs", "_static", "table")

# ---- configuration --------------------------------------------------------
# Tables to generate. Per table:
#   label         \label{...} anchor in the tex (searched verbatim)
#   tabular       0-based index of the tabular inside the table environment
#   header_rows   number of leading tex rows that form the header (skipped when
#                 header_override is set, otherwise parsed)
#   header_override  optional list of markdown header cells emitted verbatim,
#                 used when the notebook header differs from the tex header
#                 (only the data values are then taken from the tex)
#   row_map       optional {first-cell -> replacement} rewrites, matched on the
#                 cleaned first cell of each data row
#   align         optional "left" to left-align every column; default is
#                 left first column, right-aligned data columns
#   out           output filename under docs/_static/table/
TABLES = [
    {
        "label": "tab:uncertainty_decompose_RD",
        "tabular": 0,
        "header_rows": 2,
        "row_map": {"baseline": r"baseline ($\xi_m = \infty$)"},
        "out": "svrd_rd_decomposition.md",
    },
    {
        "label": "tab:uncertainty_decomopose_Temp",  # sic: label typo in tex
        "tabular": 0,
        "header_rows": 2,
        "row_map": {"baseline": r"baseline ($\xi_m = \infty$)"},
        "out": "scgw_emissions_decomposition.md",
    },
    {
        # paper Table 3 -- drift distortions. The notebook keeps its own header
        # ($h_k$/$h_r$) and row labels (more/less aversion); only the four drift
        # values are pulled from the tex.
        "label": "h_values_initial",
        "tabular": 0,
        "header_rows": 1,
        "header_override": ["", "$h_k(X0)$", "$h_r(X0)$"],
        "row_map": {
            "0.05": r"more aversion ($\xi_m = .05$)",
            "0.1": r"less aversion ($\xi_m = .1$)",
        },
        "align": "left",
        "out": "drift_distortions.md",
    },
    {
        # paper Table 6 -- flow decomposition, one-jump specification. The tex
        # two-row header ("R&D"/"capital" over "investment"/"investment") is
        # space-joined in the notebook, so the header is given explicitly.
        "label": "tab:only_tech_jump",
        "tabular": 0,
        "header_rows": 2,
        "header_override": ["$\\xi_m$", "flow i", "flow ii", "flow iii",
                            "sum", "R&D investment", "capital investment"],
        "row_map": {
            "0.05": r"$0.05$ more aversion",
            "0.1": r"$0.10$ less aversion",
            r"$\infty$": r"$\infty$ baseline",
        },
        "align": "right",
        "out": "flow_decomposition_one_jump.md",
    },
    {
        # paper Table 7 -- non-monotone SVRD vs xi. The tex is transposed
        # (xi across columns); the notebook lists xi down the rows. The xi
        # values become the first output column and are wrapped in math.
        "label": "table:nonmonotone",
        "tabular": 0,
        "transpose": True,
        "header_override": ["$\\xi_m$", "SVRD", "R&D investment / output"],
        "row_map": {
            "0.10": r"$0.10$", "0.05": r"$0.05$", "0.01": r"$0.01$",
            "0.009": r"$0.009$", "0.008": r"$0.008$", "0.007": r"$0.007$",
        },
        "align": "right",
        "out": "svrd_nonmonotone.md",
    },
]


def die(msg):
    sys.stderr.write("ABORT: %s\n" % msg)
    sys.exit(2)


# ---- tex hygiene ----------------------------------------------------------
def strip_comments(tex):
    """Remove \\begin{comment} blocks and % line comments (keeping \\%)."""
    tex = re.sub(r"\\begin\{comment\}.*?\\end\{comment\}", "", tex, flags=re.S)
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", ln) for ln in tex.splitlines())


def find_table_env(tex, label):
    envs = re.findall(r"\\begin\{table\}.*?\\end\{table\}", tex, flags=re.S)
    hits = [e for e in envs if ("\\label{%s}" % label) in e]
    if len(hits) != 1:
        die("label %s matched %d live table environments (expected exactly 1)"
            % (label, len(hits)))
    return hits[0]


def get_tabular(env, idx, label):
    tabs = re.findall(r"\\begin\{tabular\}.*?\\end\{tabular\}", env, flags=re.S)
    if idx >= len(tabs):
        die("tabular index %d out of range for %s (found %d)"
            % (idx, label, len(tabs)))
    return tabs[idx]


# ---- cell-level cleanups --------------------------------------------------
def split_cells(row):
    """Split a tabular row on unescaped & (so R\\&D stays one cell)."""
    return [c.strip() for c in re.split(r"(?<!\\)&", row)]


def lead_zero(s):
    """.0063 -> 0.0063 and -.184 -> -0.184, without touching 3.16."""
    return re.sub(r"(?<![\d.\w])(-?)\.(\d)", r"\g<1>0.\g<2>", s)


def clean(s):
    s = re.sub(r"\\hspace\{[^}]*\}", "", s)
    s = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", s)
    s = s.replace(r"\%", "%").replace(r"\&", "&")
    s = lead_zero(s)
    return s.strip()


def expand_multicol(cell):
    m = re.match(r"\\multicolumn\{(\d+)\}\{[^}]*\}\{(.*)\}$", cell.strip())
    if m:
        return [m.group(2)] * int(m.group(1))
    return [cell]


def expand_row(cells):
    out = []
    for c in cells:
        out.extend(expand_multicol(c))
    return out


# ---- tabular -> markdown --------------------------------------------------
def build_header(rows, cfg):
    """Return the list of markdown header cells for this table."""
    if cfg.get("header_override"):
        return list(cfg["header_override"])

    header = [expand_row(split_cells(r)) for r in rows[:cfg["header_rows"]]]
    if cfg["header_rows"] == 1:
        return [clean(c) for c in header[0]]
    if cfg["header_rows"] == 2:
        # two-row header: a group row (with \multicolumn spans) over a sub row;
        # combine as "group <br> (sub)" per column.
        group, sub = header[0], header[1]
        head = []
        for i in range(len(sub)):
            g = clean(group[i]) if i < len(group) else ""
            s = clean(sub[i])
            head.append("%s <br> (%s)" % (g, s) if g else s)
        return head
    die("unsupported header_rows=%d for %s (set header_override)"
        % (cfg["header_rows"], cfg["label"]))


def parse_rows(tab):
    """Return the tabular's content rows (rule/hline rows dropped)."""
    body = re.search(r"\\begin\{tabular\}\{[^}]*\}(.*)\\end\{tabular\}",
                     tab, flags=re.S).group(1)
    rows = []
    for r in body.split(r"\\"):
        r = re.sub(r"\\(?:top|mid|bottom)rule|\\hline", "", r)
        r = re.sub(r"\\cmidrule(\(lr\))?\{[^}]*\}", "", r).strip()
        if r:
            rows.append(r)
    return rows


def alignment(ncol, mode):
    if mode == "left":
        return ["---"] * ncol
    if mode == "right":
        return ["---:"] * ncol
    return ["---"] + ["---:"] * (ncol - 1)  # default: label left, data right


def tabular_to_md(tab, cfg):
    rows = parse_rows(tab)

    if cfg.get("transpose"):
        # tex lays the table out wide (e.g. xi across columns); the notebook
        # wants it tall. Transpose the cell grid; the header must be given
        # explicitly since the tex row labels become column headers.
        if not cfg.get("header_override"):
            die("transpose requires header_override for %s" % cfg["label"])
        grid = [list(col) for col in zip(*[split_cells(r) for r in rows])]
        head = list(cfg["header_override"])
        data = grid[1:]
    else:
        head = build_header(rows, cfg)
        data = [split_cells(r) for r in rows[cfg["header_rows"]:]]

    ncol = len(head)
    row_map = cfg.get("row_map", {})
    rule = alignment(ncol, cfg.get("align"))

    lines = ["| " + " | ".join(head) + " |",
             "|" + "|".join(rule) + "|"]
    for cells in data:
        cells = [clean(c) for c in cells]
        if cells and cells[0] in row_map:
            cells[0] = row_map[cells[0]]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


# ---- driver ---------------------------------------------------------------
def generate():
    tex = strip_comments(open(TEX, encoding="utf-8").read())
    out = {}
    for cfg in TABLES:
        env = find_table_env(tex, cfg["label"])
        tab = get_tabular(env, cfg["tabular"], cfg["label"])
        out[cfg["out"]] = tabular_to_md(tab, cfg)
    return out


def main():
    check = "--check" in sys.argv[1:]
    if not os.path.exists(TEX):
        die("paper tex not found at %s" % TEX)

    generated = generate()
    stale = False
    for name, md in generated.items():
        path = os.path.join(OUTDIR, name)
        current = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if current == md:
            sys.stdout.write("[up-to-date] %s\n" % name)
            continue
        stale = True
        if check:
            sys.stdout.write("[STALE] %s\n" % name)
            for line in difflib.unified_diff(
                    (current or "").splitlines(), md.splitlines(),
                    lineterm="", n=0):
                sys.stdout.write("    " + line + "\n")
        else:
            if not os.path.isdir(OUTDIR):
                os.makedirs(OUTDIR)
            with open(path, "w", encoding="utf-8") as f:
                f.write(md)
            sys.stdout.write("[written] %s\n" % name)

    if check and stale:
        sys.stdout.write("\nGenerated tables are out of date. "
                         "Run: python tools/sync_tables_from_tex.py\n")
        sys.exit(1)
    sys.stdout.write("\nDone.\n")


if __name__ == "__main__":
    main()
