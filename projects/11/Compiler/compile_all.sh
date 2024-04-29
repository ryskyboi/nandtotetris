#!/bin/bash

find .. -maxdepth 1 -type d ! -name . ! -name 'Compiler' | while read -r dir; do
    echo "Compiling" $dir
    eval poetry run python JackAnalyzer.py $dir
done
