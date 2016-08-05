#! /usr/bin/env bash

FILE1=${1:-sample-partA.csv}
FILE2=${2:-sample-partB.csv}
output=${3:-final-output.csv}
stats=${4:-statistics.txt}

# generate statistics
if [ -e ${stats} ]; then
    rm ${stats}
fi
for file in $FILE{1,2}; do
    echo 'Lines in '${file}': '$((`wc -l ${file} | cut -d' ' -f1` - 1)) >> ${stats}
done

# append partB marks and total marks to each line of partA
while read line;
do
    rollnum=`echo ${line} | cut -d, -f1`
    marks_a=`echo ${line} | cut -d, -f2`
    if [ `echo ${line} | grep -c 'RollNum'` -eq 1 ]; then
        line='RollNum, part A, Name, part B, Total, IsTied'
        sum_data=${line}
        continue
    fi
    if [ `echo ${line} | cut -d, -f2` -gt 20 ]; then
        line=${line}', '`grep ${rollnum} ${FILE2} | cut -d, -f2`
        # calculate sum
        marks_b=`echo ${line} | cut -d, -f4`
        line=${line}', '$((marks_a + marks_b))
    else
        line=${line}', NC, '${marks_a}
    fi
    sum_data=${sum_data}$'\n'${line}
done < ${FILE1}

# sort the non-header lines and find ties and non-tied scores
sorted=`echo "${sum_data}" | tail -n+2 | sort -n -k5`
no_tie=`echo "${sorted}" | uniq -f4 -u | sed 's/$/, No/g'`
tie=`echo "${sorted}" | uniq -f4 -D | sed 's/$/, Yes/g'`

# sort based on roll number
sorted=${no_tie}$'\n'${tie}
sorted=`echo "${sorted}" | sort -n -k1`

# append sorted data to header line
output_data=`echo "${sum_data}" | head -n1`
output_data=${output_data}$'\n'${sorted}

# reorder the columns, beautify them for final output
echo "${output_data}" | awk -F, '{print $1", "$3", "$2", "$4", "$5", "$6}' | tr -s ' ' > ${output}
