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
    echo 'Lines in '${file}': '$((`wc -l ${file} | cut -d' ' -f1` - 0)) >> ${stats}
done

# append partB marks and total marks to each line of partA
while read line;
do
    rollnum=`echo ${line} | cut -d, -f1`
    marks_a=`echo ${line} | cut -d, -f2`
    if [ `echo ${line} | grep -c 'RollNum'` -eq 1 ]; then
        line='Sr.Num., RollNum, part A, part B, Total, IsTied'
        sum_data=${line}
        continue
    fi
    if [ ${marks_a} -ge 20 ]; then
        line=${line}', '`grep ${rollnum} ${FILE2} | cut -d, -f2`
        # calculate sum
        marks_b=`echo ${line} | cut -d, -f3`
        line=${line}', '$((marks_a + marks_b))
    else
        line=${line}', NC, '${marks_a}
    fi
    sum_data=${sum_data}$'\n'${line}
done < ${FILE1}

# check if there is no header
if [ `echo "${sum_data}" | head -n1 | wc -w` -eq 0 ]; then
    line='Sr.Num., RollNum, part A, part B, Total, IsTied'
    line=${line}$'\n'`echo "${sum_data}" | tail -n+2`
    sum_data=`echo "${line}"`
fi

# sort the non-header lines and find ties and non-tied scores
sorted=`echo "${sum_data}" | tail -n+2 | sort -n -k4`
no_tie=`echo "${sorted}" | uniq -f3 -u | sed 's/$/, No/g'`
tie=`echo "${sorted}" | uniq -f3 -D | sed 's/$/, Yes/g'`

# sort based on decreasing total marks
if [ `echo "${no_tie}" | wc -w` -eq 0 ]; then
    sorted=${tie}
else
    if [ `echo "${tie}" | wc -w` -eq 0 ]; then
        sorted=${no_tie}
    else
        sorted=${no_tie}$'\n'${tie}
    fi
fi
sorted=`echo "${sorted}" | sort -n -k4 -r | awk -F, '{$1=++i FS $1;}1' OFS=,`

# append sorted data to header line
output_data=`echo "${sum_data}" | head -n1`
output_data=${output_data}$'\n'${sorted}

# reorder the columns, beautify them for final output
echo "${output_data}" | tr -s ' ' | sed 's/, /,/g' > ${output}
# awk -F, '{print $1","$2","$3","$4","$5","$6}' |
