#! /usr/bin/env bash

RESULT=${1:-compiled-output.csv}
PART_A=${2:-sample-partA.csv}
PART_B=${3:-sample-partB.csv}
OUTPUT=${4:-final-output.csv}
STATS=${5:-statistics.txt}
TEMPLATE_OUT=${6:-final-output.csv}
TEMPLATE_STAT=${7:-statistics.txt}
MAX_MARKS=${8:-10}

# prepare output file
echo "rollnum-header,mark-header" > ${RESULT}

for file in *.sh; do
    if [ `basename ${0}` == ${file} ]; then
        continue;
    fi
    name=${file%.*}
    if [ ! -d ${name} ]; then
        mkdir ${name}
    fi
    mv ${file} ${name}
    file=${name}'/'${file}
    output=${name}'/'${OUTPUT}
    stats=${name}'/'${STATS}
    bash ${file} ${PART_A} ${PART_B} ${output} ${stats}

    # count differences
    errors_out=`diff -w ${TEMPLATE_OUT} ${output} | grep -c '>'`
    errors_stat=`diff -w ${TEMPLATE_STAT} ${stats} | grep -c '>'`
    errors=$((errors_out + errors_stat))

    # count files created
    number=`ls -1 ${name} | wc -l`

    # calculate marks, assume each error costs 1 mark
    marks=$((MAX_MARKS - number + 3 - errors))  # 3 files are OK

    # save output
    echo ${name},${marks} >> ${RESULT}

    # for testing purpose only. In production, remove any file
    # called testing from the current directory
    if [ -e testing ]; then
        mv ${file} ${name}.sh
    fi
done
