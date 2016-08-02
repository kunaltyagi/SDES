# BASH assignment

Two bash assignments have to be submitted by 8th August (Monday) morning 8am. Exact submission procedure (moodle or email) will be intimated by Friday. Please read the full assignment and start immediately to avoid last minute under-sleepings.

# Exercise 1

Using bc, grep, for, and shell variables, and sed write a bash script that achieves the following. For the CEED exam, students appear for an objective part: part A (out of 40), and a subjective part: part B (out of 60).

Part B is corrected only if students get more than 20 in part A.

Take two files: partA.csv and partB.csv in which first column is a unique roll number and second column is marks. partA.csv has X number of lines (number of candidates) and partB.csv has Y number of lines (those who got more than 20 marks).

RollNum is just a number of 6 digits: no spaces, no commas, just numbers: and unique.

Generate an final-output.csv file that has following columns and sorted according to the the total, and the Serial number is a running number, but if there is a tie in the total, then the IsTied column will tell Yes/No:

Sr.Num., RollNum, Name, part A, part B, Total, IsTied:Yes-No

1, 101010, Name of topper, 32, 56, 88, No

2, 121010, Name of second, 33, 50, 83, No

...

56, 113013, Name of last person, 10, NC, 10, No

## Note:

*   All students get only integer marks.

*   NC in the part B marks stands for Not-Corrected

*   If somebody gets "NC" in part B, the reason would be that that person

    got strictly less than 20 in part A, and hence his/her rollnumber would not have got found in partB.csv

*   Generate some statistics in statistics.txt file which has

    How many in partA.csv, how many in partB.csv,

*   10 marks for this assignment

*   Creation of temporary files is OK. -1 mark for each file created/overwritten.

# Exercise 2

A class has amore than 50 students. Each student (with a unique rollnumber) submits a bash script (rollnumber.sh) that achieves what is in Exercise 1 above. Write a script that

*   takes rollnumber.sh as the argument,

*   makes a directory called rollnumber and moves the file.sh there and

*   runs each rollnumber.sh on dummy files partA.csv and partB.csv

*   compares against correct file for templates

*   awards a mark out of 10 (depending on the grading rule)

*   makes ONE csv file for all rollnumbers with columns

    rollnum-header, mark-header rollnum, mark rollnum, mark rollnum, mark

Your script will look for all sh files in that directory and run on each sh file (with rollnumber as the directory, moving the sh file into that directory.

Use for, cmp or diff (with options of exit status, etc) and if.

This assignment is also 10 marks.

Both assignments together have weightage 3% (and equal weightage each).
