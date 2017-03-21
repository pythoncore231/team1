# -*- coding: utf-8 -*-

input_number = int(raw_input(u"Введіть число: "))
counter = 0

if input_number == 2:
    print u"{} являється простим числом".format(input_number)

elif input_number < 2 or input_number > 2 and input_number % 2 == 0:
    print u"{} не є простим числом".format(input_number)

else:
    for i in range(3, input_number):
        if input_number % i == 0:
            counter += 1
    if counter > 0:
        print u"{} не є простим числом".format(input_number)
    else:
        print u"{} являється простим числом".format(input_number)
