import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = (3 + math.exp(y - 1))/(1 + x * x * (math.fabs(y - math.tan(z))))
b = 1 + math.fabs(y - x) + ((y - x) ** 2) / 2. + ((math.fabs(y - x)) ** 3) / 3.

print "a =", a
print "b =", b
