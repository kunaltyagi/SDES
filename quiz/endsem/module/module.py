#!/usr/bin/env python
# -*- coding: utf-8 -*-

def module_filename(module):
    import sys
    if type(module) != type(sys):
        raise TypeError
    if sys.version_info[0] == 3:
        specs = module.__spec__
        return 'builtin' if specs.origin == 'built-in' else specs.origin
    if hasattr(module, '__file__'):
        return module.__file__
    return 'builtin'

if __name__ == '__main__':
    import math
    import os
    print(module_filename(math))
    print(module_filename(os))
