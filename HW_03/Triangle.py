'''
Created on Mar 16, 2017

@author: vodachuk
'''
from math import sqrt
a = input("a = ")
b = input("b = ")
c = input("c = ")
p = (a + b + c) / 2
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print "P = {:<5}".format(str(a + b + c)), "S = {:<5}".format(str(sqrt(p * (p - a) * (p - b) * (p - c))))
else:
    print "Incorrect input"
