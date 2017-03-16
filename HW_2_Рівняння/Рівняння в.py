import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = (1 + y) * (x + y / (x * x + 4.)) / (math.exp(- x - 2) + 1 / (x * x + 4.))
b = (1 + math.cos(y - 2)) / ((x ** 4 / 2.) + math.sin(z) ** 2)

print "a =", a
print "b =", b
