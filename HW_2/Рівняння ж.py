import math

x = float(input('Input x = '))
y = float(input('Input y = '))
z = float(input('Input z = '))

a = math.log1p(math.fabs((y - math.fabs(x) ** 0.5) * (x - y / (z + x * x / 4))))
b = x - x * x / math.factorial(3) + x ** 5 / math.factorial(5)

print "a =", a
print "b =", b
