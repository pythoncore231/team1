#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

# 1
print "Multiplication of digits of a natural number:"
number = 1234
strNumber = str(number)
print int(strNumber[0]) * int(strNumber[1]) * int(strNumber[2]) * int(strNumber[3])

# 2
print "Exchange of variables:"
a = 4
b = 5
a, b = b, a
print a, b
a = a + b
b = a - b
a = a - b
print a, b

# 3
print "Math exercises:"
print "Input x:"
x = float(input())
print "Input y:"
y = float(input())
print "Input z:"
z = float(input())
#a
a = (sqrt(fabs(x-1)) - fabs(y)**(1./3)) / (1 + x**2/2 + y**2/4)
b = x * (atan(z) + e**-(x+3))
print "a) a = {}; b = {}".format(a, b)
#б
a = (3 + e**(y+1)) / (1 + x**2*(fabs(y-tan(z))))
b = 1 + fabs(y-x) + (y-x)**2/2 + fabs(y-x)**3/3
print "б) a = {}; b = {}".format(a, b)
#в
a = (1 + y) * ((x+y/(x**2+4)) / (e**(-x-2)+1/(x**2+4)))
b = (1 + cos(y-2)) / (x**4/2 + sin(z)**2)
print "в) a = {}; b = {}".format(a, b)
#г
a = y + x / (y**2 + fabs(x**2/(y+x**3/3)))
b = 1 + tan(z/2)**2
print "г) a = {}; b = {}".format(a, b)
#д
a = (2*cos(x-pi/6)) / (1./2 + sin(y)**2)
b = 1 + z**2 / (3 + z**2/5)
print "д) a = {}; b = {}".format(a, b)
#e
a = (1 + sin(x+y)**2) / (2 + fabs(x - 2*x/(1+x**2*y**2))) + x
b = cos(atan(1/z))**2
print "e) a = {}; b = {}".format(a, b)
#ж
a = log(fabs((y-sqrt(fabs(x)))*(x-y/(z+x**2/4))))
b = x - x**2/factorial(3) + x**5/factorial(5)
print "ж) a = {}; b = {}".format(a, b)