from math import *

x = input("x = ")
y = input("y = ")
z = input("z = ")

print "---------------------------------" * 10
#form A
a = (sqrt(fabs(x - 1)) - fabs(y)**(1 / 3)) / (1 + (x**2) / 2 + (y**2) / 4)
b = x*(atan(z) + exp(-(x + 3)))
print a,b


print "---------------------------------" * 10
# form B
a = (3 + exp(y - 1)) / ((1 + (x**2)) * fabs(y - tan(z)))
b = 1 + fabs(y - x) + ((y + x) **2 / 2) + (fabs(y - x)**3 / 3)
print a,b


print "---------------------------------" * 10
# form C
a = (1 + y) * (((x + y / ((x ** 2) + 4))) / ((exp(- x - 2) + 1) / ((x ** 2) + 4)))
b = (1 + cos(y - 2)) / ((x ** 4) / 2 + (sin(z) **2))

print a,b

print "---------------------------------" * 10
#form D

a = y + x / ((y ** 2) + fabs((x ** 2) / (y + (x**3) / 3)))
b = (1 + (tan(z / 2)) ** 2)

print a,



print "---------------------------------" * 10
#form E
a = (2 * cos(x - pi / 6)) / (1 / 2 + (sin(y) ** 2))
b = 1 + ((z ** 2) / (3 + (z ** 2) / 5))

print a,b


print "---------------------------------" * 10
#form F

a = ((1 + sin(x + y) ** 2) / (2 + fabs(x - 2 * 2 / (1 + (x **2) * (y ** 2))))) + x
b = cos(atan(1 / z)) ** 2

print a,b



print "---------------------------------" * 10
#form G
a = log(fabs((y - sqrt(fabs(x))) * (x - y / (z + (x ** 2) / 4))))
b = x - ((x ** 2) / factorial(3)) + ((x ** 5) / factorial(5))


print a,b