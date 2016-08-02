#!/usr/bin/env bash

count=$(wc -l $1 | cut -d' ' -f1)
echo $count
echo $1:$count > $2
