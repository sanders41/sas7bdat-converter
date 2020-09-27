#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --cov=sas7bdat_converter --cov-report=term-missing
