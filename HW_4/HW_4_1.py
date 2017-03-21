# -*- coding: utf-8 -*-

input_number = int(raw_input(u"Введіть число від 1 до 36: "))
if input_number < 1 or input_number > 36:
    print u"Число не відповідає умові"
a = int
for number_1 in range(1, 10):
    for number_2 in range(10):
        for number_3 in range(10):
            for number_4 in range(10):
                a = (number_1 + number_2 + number_3 + number_4)
                if a == input_number:
                    print u"{}{}{}{}".format(number_1, number_2, number_3, number_4)

