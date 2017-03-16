'''
Created on Mar 14, 2017
@author: vodachuk
'''
from math import *
x = input("x = ")
y = input("y = ")
z = input("z = ")
# a)
a = (((fabs(x - 1.0)) ** (0.5)) - ((fabs(y)) ** (1.0/3.0)))/(1 + (x ** 2.0)/2.0 + (y ** 2.0)/4.0)
b = x * (atan(z) + exp(-(x + 3.0)))
print "a) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# b)
a = (3.0 + exp(y - 1.0)) / (1.0 + (x ** 2.0) * fabs(y - tan(z)))
b = 1.0 + fabs(y - x) + (((y - x) ** 2.0) / 2.0) + (((y - x) ** 3.0) / 3.0)
print "b) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# c)
a = (1.0 + y) * (((x + y) / (x ** 2.0 + 4.0)) / (exp(-x - 2.0) / (x ** 2.0 + 4.0)))
b = (1.0 + cos(y - 2.0)) / ((x ** 4.0) / (2.0 + (sin(z) ** 2.0)))
print "c) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# d)
a = y + x / ((y ** 2.0) + fabs((x ** 2.0) / (y + (x ** 3.0) / 3.0)))
b = (1.0 + (tan(z / 2.0)) ** 2.0)
print "d) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# e)
a = (2.0 * cos(x - pi / 6.0)) / (1. / 2. + (sin(y) ** 2.))
b = 1 + (z ** 2.) / (3. + (z ** 2.) / 5.)
print "e) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# f)
a = ((1. + (sin(x + y) ** 2.)) / (2. + abs(x - (2. * x) / (1. + (x ** 2.) * (y ** 2.))))) + x
b = (cos(atan(1. / z))) ** 2.
print "f) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# g)
a = log(abs((y - sqrt(abs(x))) * (x - y / (z + (x ** 2.) / 4.))))
b = x - ((x ** 2.) / factorial(3.)) + ((x ** 5.) / factorial(5.))
print "d) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))