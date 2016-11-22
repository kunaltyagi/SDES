#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def find_non_alpha(s):
    from string import ascii_lowercase, ascii_uppercase, whitespace
    return set([x for x in s if x not in ascii_lowercase + ascii_uppercase + whitespace])

def sort_list(data_list):
    tmp = sorted(data_list, key=lambda x: x[0])
    return sorted(tmp, key=lambda x: x[1], reverse = True)

def word_freq(string):
    work_str = string.lower()
    remove = find_non_alpha(work_str)
    words = work_str.split()
    lst = []
    for word in words:
        w = [x for x in word if x not in remove]
        clean_word = ''
        for letter in w:
            clean_word += letter
        lst.append(clean_word)
    dct = []
    for word in lst:
        if word != '':
            dct.append((word, lst.count(word)))
    return sort_list(list(set(dct)))

class Student(object):
    def __init__(self, name, roll_num, score):
        self.name = name
        self.roll_num = int(roll_num)
        self.score = int(score)

def student_info(csv_str):
    records = [x.split(',') for x in csv_str.split('\n')]
    for r in records:
        yield Student(r[0].strip(), r[1].strip(), r[2].strip())

def main():
    pass

if __name__ == "__main__":
    main()
