# -*- coding: utf-8 -*-
from fixer.data_manager import get_rates
from utils.print_data import check_date_base, yesterday, print_dict, last_3_days, print_exchange


def checked_rates(date=None, base=None):
    if check_date_base(date, base):
        return get_rates(date, base)
    else:
        print "Either date or base are invalid."

print "last_3_days"
# із базового словника беремо запис останньої дати
last_date = checked_rates(None, "USD")["date"]

# створюємо список з дат для 3 останніх днів, за допомогою функції yesterday
list_3_days = [yesterday(yesterday(last_date)), yesterday(last_date), last_date]

# створюємо список базових словників курсу долара для кожної дати зі списку використовуючи list comprehension
list_dict = [checked_rates(date, "USD") for date in list_3_days]

# роздруковуємо курс долара для кожної валюти за останні 3 дні
last_3_days(list_dict)

# DONE
# вивести курс за 25/01/2017 для TRY
print
print "try_2017_01_25"
print_dict(checked_rates("2017-01-25", 'TRY'))

# DONE
# вивести день, в який був самий вигідний курс для обміну IDR на CZK, у проміжку з 1/01/2013 по 25/01/2013
print
print "Profit!"

# створюємо список дат з 1/01/2013 по 25/01/2013 використовуючи list comprehension
date_basis = "2013-01-"
list_of_date = ["{}{}{}".format(date_basis, 0, i) if len(str(i)) < 2
                else "{}{}".format(date_basis, i) for i in range(1, 26)]

# створюємо список значень курсу CZK для IDR з 1/01/2013 по 25/01/2013 використовуючи list comprehension
list_of_value = [print_exchange(1, checked_rates(j, 'IDR'), 'CZK')for j in list_of_date]

# визначаємо індекс мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
min_index = list_of_value.index(min(list_of_value))

# роздруковуємо дату та значення за індексом мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
print "At {} you could buy 1 IDR by {} CZK.".format(list_of_date[min_index], min(list_of_value))
