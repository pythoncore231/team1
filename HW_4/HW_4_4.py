# -*- coding: utf-8 -*-

input_number = raw_input(u"Введіть число: ")
result = 0

for i in input_number:
    result += int(i) ** 3
print u"Сума кубів цифр заданого натурального числа дорівнює {}". format(result)
