#! /usr/bin/env bash

for file in *.sh; do
    name=${file%.*}
    mkdir ${name}
    mv ${file} ${name}
done
