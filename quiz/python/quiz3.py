#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nonnegative(func):
    def returnNone(n):
        return None if n < 0 else func(n)
    return returnNone

def twice(func):
    def wrapper(*args, **kwargs):
        return 2*func(*args, **kwargs)
    return wrapper

class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return 'Vector('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'
        # 'Vector(%s, %s, %s)'%(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ == __mul__

    def norm(self):
        import math
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y*other.z-self.z*other.y,
                self.z*other.x-self.x*other.z,
                self.x*other.y-self.y*other.x)


def strip_string(arg):
    oldchar = ''
    newstr=''
    for char in arg:
        if not char.isalnum() and char != '/':
            if oldchar == '_':
                continue
            else:
                char = '_'
                oldchar = char
                newstr += char
        else:
            oldchar = char
            newstr += char
    return newstr

def strip_string2(arg):
    import string
    allowed = string.ascii_lowercase + string.ascii_uppercase + '_/' + '0123456789'
    result = ''
    for c in text:
        if c in allowed:
            result += c
            old = c
        else:
            if old != '_':
                old = '_'
                result += old
                # doesnt work
    return result
