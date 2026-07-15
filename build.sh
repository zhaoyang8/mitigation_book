#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "Building mitigation_book  $(date)"
start=$(date +%s)

# Activate the legacy Jupyter Book environment when conda is available.
# Create it with:
#   conda create -n jb015 python=3.10 -y
#   conda activate jb015
#   python -m pip install -r docs/requirements.txt
if [ "${CONDA_DEFAULT_ENV:-}" != "jb015" ] && command -v conda >/dev/null 2>&1; then
  eval "$(conda shell.bash hook)"
  if conda env list | awk '{print $1}' | grep -qx "jb015"; then
    conda activate jb015
  fi
fi

jb_cmd="jupyter-book"
if command -v jb >/dev/null 2>&1; then
  jb_cmd="jb"
fi

version="$("$jb_cmd" --version | awk 'NR == 1 {print $NF}')"
case "$version" in
  0.*) ;;
  *)
    echo "Expected legacy jupyter-book 0.x, found: $version" >&2
    echo "Create and activate jb015, then install docs/requirements.txt." >&2
    exit 1
    ;;
esac

(
  cd docs
  "$jb_cmd" clean .
  "$jb_cmd" build . --all
)
touch docs/_build/html/.nojekyll

end=$(date +%s)
printf "Elapsed: %02d min %02d sec\n" $(( (end-start)/60 )) $(( (end-start)%60 ))
