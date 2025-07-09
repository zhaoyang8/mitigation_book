#!/usr/bin/env bash
set -euo pipefail

echo "Building mitigation_book  $(date)"
start=$(date +%s)

# activate the environment you created above
source ~/miniconda3/bin/activate jb        # adjust for your install path
# or: . ~/…/venv/bin/activate              # if you prefer venv + pip

# build the book
jupyter-book build ~/Desktop/two_capital_book/mitigation_book/docs
touch docs/.nojekyll

# simple timing info
end=$(date +%s)
printf "Elapsed: %02d min %02d sec\n" $(( (end-start)/60 )) $(( (end-start)%60 ))