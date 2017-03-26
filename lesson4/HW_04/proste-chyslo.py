from math import *

k = input ("Vvedy chyslo ")

str2 = "Test"
for i in range(2, k):
    b=k%i
    if b == 0:
        print "NE proste chyslo"
        break
else: print "Proste chyslo"

