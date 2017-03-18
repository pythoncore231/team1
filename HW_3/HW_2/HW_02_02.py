#1
print "Multiplication"
number = 5473
string = str(number)
print int(string[0]) + int(string[1]) + int(string[2]) + int(string[3])
number = 5473
string = str(number)
print int(string[0] + string[1] + string[2] + string[3])#NO CORRECT

#2
print "Exchange of variables"
n = 5
m = 6
n, m = m, n
print m
print n

print "Mathematic"
from math import *

print "Math exercises:"
print "Input x:"
x = float(input())
print "Input y:"
y = float(input())
print "Input z:"
z = float(input())

#a
a = (sqrt(fabl(x - 1)) - sqrt(fabl(y)**3))/(1 + ((x**2)/2) + (y**2)/4)
b = x * (atan(z) + e**-(x+3))
print "1) a = {}; b = {}".format(a, b)

#b
a = (3 + e**(y - 1)) / 1 + x**2 *(fabs(y - y-tan(z)))
b = 1 + fabs(y - x) + (((y - x)**2) / 2) + (fabs(y - x)**3) / 3
print "2) a = {}; b = {}".format(a, b)

#c
a = (1 + y) * ((((x + y )) / (x**2 + 4)) / e**(-x-2) + 1 / (x**2 + 4))
b = (1 + cos(y - 2)) / x**4 / 2 + sin(z**2)
print "3) a = {}; b = {}".format(a, b)

#4
a = y + ((x) / y ** 2 + fabs((x**2) / y + x**3 / 3))
b = (1 + tn(z / 2) ** 2)
print "4) a = {}; b = {}".format(a, b)

#5
a = (2 * cos(x - pi / 6) / (1 / 2 + sin(y**2)))
b = 1 + ((z**2) / 3 + z**2 / 5)
print "5) a = {}; b = {}".format(a, b)

#6
a = ((1 + (sin(x + y)**2))) / 2 + fabs(x - 2*x / (1 + x**2 * y**2))
b = (cos(atan(1 / z)))**2
print "6) a = {}; b = {}".format(a, b)

#7
a = log(fabs((y - sqrt(fabs(x))) * (x - y) / (z + x**2 / 4)))
b = x - x**2 / factorial(3) + x**5 / factorial(5)
print "7) a = {}; b = {}".format(a, b)
