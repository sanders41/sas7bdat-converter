#!/usr/bin/env bash

set -e
set -x

mypy sas7bdat_converter
black sas7bdat_converter tests --check
