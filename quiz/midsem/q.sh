#! /usr/bin/env bash

OUTFILE='final_out.txt'
INFILE=$1

for line in $OUTFILE:
    if [ `echo $line | wc -w` -ne 0 ];
    then
        echo $line >> $OUTFILE;
    fi
    echo >> $OUTFILE
