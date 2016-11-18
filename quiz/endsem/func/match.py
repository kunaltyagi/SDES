#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_functions(rel_path):
    import os
    import re
    f_list = list()
    for dirpath, dirname, filenames in os.walk(rel_path):
        for f in filenames:
            if f.split('.')[-1] == 'py':
                with open(dirpath + '/' + f, 'r') as inFile:
                    line_no = 1
                    lines = inFile.readlines()
                    for line in lines:
                        line = line.strip()
                        match = re.search('^def', line)
                        if match is not None:
                            f_list.append((dirpath + '/' + f, line_no, line))
                        line_no += 1
    return f_list


if __name__ == "__main__":
    print(find_finctions('./'))
