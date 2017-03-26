from math import *

k = input ("Vvedy chyslo ")
F1=1
F2=1
print F1
print F2
a=2
for i in range(k):
    fsum=F1+F2
    F1=F2
    F2=fsum
    a +=1
    print fsum
    if fsum+F1 > k:
        break
print a, " Chysel fibonachi"
