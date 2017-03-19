# 3 Quadratic equation

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b ** 2 - 4 * a * c
if D < 0:
    print "roots of a quadratic equation does not exist"
elif D == 0:
    print "x = {}".format((b + sqrt(D)) / 2 * a)
else:
    print "x1 = {}".format((b + sqrt(D)) / 2 * a)
    print "x2 = {}".format((b - sqrt(D)) / 2 * a)