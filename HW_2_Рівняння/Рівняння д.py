import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = (2 * math.cos(x - math.pi / 6)) / ((1. / 2) + math.sin(y) ** 2)
b = 1 + (z * z / (3 + z * z / 5))

print "a =", a
print "b =", b
