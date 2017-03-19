# 4 Triangle

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if b < a and c < a and b + c > a or \
    a < b and c < b and a + c > b or \
    a < c and b < c and a + b > c:
	print True
	pp = (a + b + c) / 2
	print "p = {}".format(pp * 2)
	print "S = {}".format(sqrt(pp * (pp - a) * (pp - b) * (pp - c)))
else:
	print False