import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = a + b + c

if (d < (2*a)) or (d < (2*b)) or (d < (2*c)):
    print("It is not a triangle")
elif (a == b == c):
    print("It is Equalateral")
elif (a == b) or (a == c) or (b == c):
    print("It's Isosceles")