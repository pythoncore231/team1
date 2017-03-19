from math import *

k = input ("Vvedy k vid 1 do 365 k = ")

k1=k%7

#print k1
if k >= 1 and k <= 365 and type(k) == int:
    print "Dani vvedeno korektno"
    if k1 == 1:
        print "Ponedilok"
    elif k1 == 2:
        print "Vivtorok"
    elif k1 == 3:
        print "Sereda"
    elif k1 == 4:
        print "Chetver"
    elif k1 == 5:
        print "Pyatnycya"
    elif k1 == 6:
        print "Subota"
    elif k1 == 0:
        print "Nedilya"
else: print "Ne korektni dani"
