#!/usr/bin/env bash

source ../.venv/bin/activate
rm ./build/ -r -f
make html
