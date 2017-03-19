#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from math import *
from types import *

# 1
string = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts."""

if len(string) > 100:
    print "Too long text"
else:
    print "Count: {}".format(string.count("a") + string.count("e") + \
                             string.count("i") + string.count("o") + \
                             string.count("u") + string.count("y"))

# 2
print "ax**2 + bx + c = 0"
a = input("a = ")
b = input("b = ")
c = input("c = ")

if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and \
        (type(c) == int or type(c) == float):
    D = b**2 - 4*a*c

    if D < 0:
        print "Коренів немає"
    elif D == 0:
        print "x = {}".format((b + sqrt(D)) / 2 * a)
    else:
        print "x1 = {}".format((b + sqrt(D)) / 2 * a)
        print "x2 = {}".format((b - sqrt(D)) / 2 * a)
else:
    print "Треба було ввести число, а Ви ввели шось не то..."