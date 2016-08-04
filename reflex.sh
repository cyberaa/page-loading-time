#!/bin/bash
reflex -r '.*\.py$' -- python tests.py 2>&1 | grep --color -E '^|^.*fail.*$'
