#!/usr/bin/env bash

set -e
set -x

mypy sas7bdat_converter
isort sas7bdat_converter tests --check-only
black sas7bdat_converter tests --check
flake8 sas7bdat_converter tests
