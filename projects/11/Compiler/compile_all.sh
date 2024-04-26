#!/bin/bash

for dir in $(find .. -maxdepth 1 -type d ! -name . ! -name 'Compiler'); do
    echo "Compiling" $dir
    eval poetry run python JackAnalyzer.py $dir
done
