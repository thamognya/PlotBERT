#!/bin/sh

if [ -d "./env/"]; then
    echo "Python venv with name env does not exist"
else
    if [["$0" == "fish"]]; then
        source ./env/bin/activate.fish
    else if [["$0" == "csh"]]; then
        source ./env/bin/activate.csh
    else
        source ./env/bin/activate
    fi

    echo "Done sourcing"
fi
