import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = ((1 + math.sin(x + y) ** 2) / (2 + math.fabs(x - 2 * x / (1 + x * x * y * y)))) + x
b = math.cos(math.atan(1 / z)) ** 2

print "a =", a
print "b =", b
