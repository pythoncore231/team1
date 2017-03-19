from math import *

a = input ("Vvedy storonu trykutnyka a = ")
b = input ("Vvedy storonu trykutnyka b = ")
c = input ("Vvedy storonu trykutnyka c = ")

if c < (a +b) and a < (c + b) and b < (c + a):
    print "Trykutnuk mojna pobuduvaty"
    P = a + b + c
    P1 = P/2
    S = (P1*((P1-a) * (P1-b) * (P1-c)))**0.5
    print "Perymetr", P
    print "Ploshcha", S

else: print "Ne mojna pobuduvaty"