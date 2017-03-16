'''
Created on Mar 16, 2017

@author: vodachuk
'''
from math import sqrt
a = input("a = ")
b = input("b = ")
c = input("c = ")
dys = b ** 2 - 4 * a * c
print dys
if dys > 0:
    print "x1 = {:<10}".format(str((b + sqrt(dys)) / (2. * a))), "\tx2 = ".format(str((b - sqrt(dys)) / (2. * a)))
elif dys == 0:
    print "x = {:<10}".format(str((b) / (2. * a)))
else:
    print "Capput"