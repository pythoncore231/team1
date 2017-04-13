# -*- coding: utf-8 -*-
import datetime
from fixer.data_manager import get_rates
from utils.print_data import check_date_base, print_dict, last_3_days, last_n_days, exchange


def checked_rates(date=None, base=None):
    if check_date_base(date, base):
        return get_rates(date, base)
    else:
        print "Either date or base are invalid."

print "last_3_days"

name_of_base = "USD"

# із базового словника беремо запис останньої дати
today = datetime.date(*map(int, checked_rates(None, None)["date"].split("-")))
# на його основі створюємо генератор трьох останніх дат
generator_of_dates = (str(today - datetime.timedelta(days=each)) for each in range(3))
# на основі якого збираємо список курсів валют за три останні дні
list_of_rates = [checked_rates(date, name_of_base) for date in generator_of_dates]
# видруковуємо курси валют за три останні дні
last_3_days(list_of_rates)

print
print "last_n_days"
n_days = 5
name_of_base = "USD"

today = datetime.date(*map(int, checked_rates(None, None)["date"].split("-")))
generator_of_dates = (str(today - datetime.timedelta(days=each)) for each in range(n_days))
list_of_rates = [checked_rates(date, name_of_base) for date in generator_of_dates]
print
last_n_days(list_of_rates)

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
list_of_value = [exchange(1, checked_rates(j, 'IDR'), 'CZK')for j in list_of_date]

# визначаємо індекс мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
min_index = list_of_value.index(min(list_of_value))

# роздруковуємо дату та значення за індексом мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
print
print "At {} you could buy 1 IDR by {} CZK.".format(list_of_date[min_index], min(list_of_value))
