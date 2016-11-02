#!/usr/bin/env bash

while IFS='' read -r -u10 line || [[ -n "$line" ]]; do
    echo "Text read is $line"
done 10<"$1"
