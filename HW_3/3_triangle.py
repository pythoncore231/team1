from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))



if c < (a + b) and a < (c + b) and b < (c + a):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print"square: ",s
else:
    print"False"