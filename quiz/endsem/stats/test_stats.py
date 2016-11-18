#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest

from stats import compute_stats_string, compute_stats

class TestComputeStatsString(unittest.TestCase):
    def test_empty_string(self):
        test_string = ""
        assert compute_stats_string(test_string) == (0, 0)

    def test_single_data(self):
        test_string = \
"""a,b,c
a,b,1
"""
        assert compute_stats_string(test_string) == (1, 0)

    def test_no_stddev(self):
        test_string = \
"""a,b,c
a,b,1
a,b,1
"""
        assert compute_stats_string(test_string) == (1, 0)

    def test_sample_data(self):
        test_string = \
"""a,b,c
a,b,1
a,b,2
a,b,0
"""
        assert compute_stats_string(test_string) == (1, 1)

    def test_online_data(self):
        test_string = \
"""name,roll_number,marks
Arun Raj,A001234, 75
Md Azeem,B001235,76
Zaheer,C001236,88
Zubizeratta,C002236,90"""
        print(compute_stats_string(test_string))
        assert compute_stats_string(test_string) == (82.25, 7.847504911329036)


class TestComputeStats(unittest.TestCase):
    def test_default_case(self):
        assert compute_stats('sample_url', True) == (82.25, 7.847504911329036)

# class TestUrl2String(unittest.TestCase):
#     def test_urllib3_called(self):
#         assert url2string('test_url').called_with('test_url)')

if __name__ == "__main__":
    unittest.main()
