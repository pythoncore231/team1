import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = y + (x / (y * y + (math.fabs(x * x / (y + x ** 3 / 3.)))))
b = 1 + math.tan(z / 2) ** 2

print "a =", a
print "b =", b
