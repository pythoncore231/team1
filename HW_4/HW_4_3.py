# -*- coding: utf-8 -*-

input_number = int(raw_input(u"Введіть натуральне число: "))

a = 1
b = 1

print u"Першими {} числами Фібоначчі є: ".format(input_number)
print a,

for i in range(input_number - 1):
    a, b = b, a + b
    print a,
