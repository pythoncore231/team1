import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = (math.fabs(x - 1.0) ** 0.5 - math.fabs(y) ** (1/3.0)) / (1.0 - ((x * x) / 2.0) + ((y * y) / 4.0))
b = x * (math.atan(z) + math.exp(-(x + 3)))

print "a =", a
print "b =", b
