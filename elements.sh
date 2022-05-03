#!/bin/bash
export ELEMENTS_USERNAME=BPInstitute
ELEMENTS_KEY=wardenpatrolsparades3 python3 elements.py
git add --all
git diff-index --quiet HEAD || git commit -m "Update citations"
git push
