from math import *

a = input ("a = ")
b = input ("b = ")
c = input ("c = ")

D = (b**2) - (4*a*c)

print D

if D < 0:
    print "Nema"
elif D == 0:
     print "Odyn"
     x = -b / (2 * float(a))
     print "X=", x
elif D > 0:
    print "dva"
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print "X1=", x1
    print "X2=", x2