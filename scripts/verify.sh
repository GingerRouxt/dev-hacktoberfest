#!/usr/bin/env bash
# Local, Tokate and CI verification; no downloads or live provider calls.
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
python3 -m unittest discover -s tests -v
bash -n scripts/verify.sh
