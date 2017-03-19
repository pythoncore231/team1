from math import *

a = input ("Vvedy rik = ")
b = input ("Vvedy misyak = ")
c = input ("vvedy den = ")

if 1 <= c <= 31 and (b%2)!=0 and  1 <= b <=12:
    print "Korektno"
    print "{}.{}.{}".format(a, b, c)
elif 1 <= c <= 28 and b == 2:
    print "Korektno"
    print "{}.{}.{}".format(a, b, c)
elif a % 4 == 0 and a % 100 != 0 or a % 400 == 0 and 1 <= c <= 29 and b == 2:
    print "Korektno"
    print "Vysokosnyi rik"
    print "{}.{}.{}".format(a, b, c)
else:
    print  "Ne korektno"