#!/usr/bin/env python
# -*- coding: utf-8 -*-

def url2string(url, debug=False):
    if debug:
        return \
"""name,roll_number,marks
Arun Raj,A001234, 75
Md Azeem,B001235,76
Zaheer,C001236,88
Zubizeratta,C002236,90"""

    import urllib3
    a = utllib3.connection_from_url(url).urlopen('GET', url)
    return a.data().decode(errors='ignore')

def compute_stats_string(data, debug=False):
    import math
    records = data.splitlines()
    if debug:
        print(records)
    marks = list()
    for line in records[1:]:
        items = line.split(',')
        marks.append(int(items[2].strip()))
    if debug:
        print(marks)
    n = len(marks)
    if n == 0:
        return 0., 0.
    mean = float(sum(marks))/n
    if n == 1:
        return mean, 0.
    stddev = math.sqrt(sum([(x - mean)**2. for x in marks])/(n-1))
    return mean, stddev

def compute_stats(url, debug=False):
    data = url2string(url, debug)
    return compute_stats_string(data, debug)
