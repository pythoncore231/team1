# -*- coding: utf-8 -*-
from fixer.data_manager import get_rates
from utils.print_data import check_date, check_base, yesterday, print_dict, last_3_days, print_3_days, \
    print_difference, print_exchange

usd = check_base("USD")

# DONE
# вивести різницю курсу валют для USD на 20 та 27 березня 2017 року
print
print "difference"
date_difference1 = get_rates(check_date("2017-03-20"), usd)
date_difference2 = get_rates(check_date("2017-03-27"), usd)


print_difference(date_difference1, date_difference2)

# DONE
# вивести суму, яку отримаєм при обміні певної суми DKK на BGN та KRW
print
print "exchange"
dkk = get_rates(None, check_base("DKK"))
print print_exchange(1, dkk, check_base("BGN"))
print print_exchange(1, dkk, check_base("KRW"))

# DONE
# вивести зміну курсу за 3 останні дні для USD
print
print "3_days"
day_1 = get_rates(check_date("2017-04-02"), usd)
day_2 = get_rates(check_date("2017-04-03"), usd)
day_3 = get_rates(check_date("2017-04-04"), usd)


print_3_days(day_1, day_2, day_3)

# альтернативний варіант без вводу дати
print
print "last_3_days"
# із базового словника беремо запис останньої дати
last_date = get_rates(None, usd)["date"]

# створюємо список з дат для 3 останніх днів, за допомогою функції yesterday
list_3_days = [yesterday(yesterday(last_date)), yesterday(last_date), last_date]

# створюємо список базових словників курсу долара для кожної дати зі списку використовуючи list comprehension
list_dict = [get_rates(date, usd) for date in list_3_days]

# роздруковуємо курс долара для кожної валюти за останні 3 дні
last_3_days(list_dict)

# DONE
# вивести курс за 25/01/2017 для TRY
print
print "try_2017_01_25"
try_2017_01_25 = print_dict(get_rates(check_date("2017-01-25"), check_base('TRY')))
print try_2017_01_25

# DONE
# вивести день, в який був самий вигідний курс для обміну IDR на CZK, у проміжку з 1/01/2013 по 25/01/2013
print
print "Profit!"

# створюємо список дат з 1/01/2013 по 25/01/2013 використовуючи list comprehension
date_basis = "2013-01-"
list_of_date = ["{}{}{}".format(date_basis, 0, i) if len(str(i)) < 2
                else "{}{}".format(date_basis, i) for i in range(1, 26)]

# створюємо список значень курсу CZK для IDR з 1/01/2013 по 25/01/2013 використовуючи list comprehension
list_of_value = [print_exchange(1, get_rates(j, 'IDR'), 'CZK')for j in list_of_date]

# визначаємо індекс мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
min_index = list_of_value.index(min(list_of_value))

# роздруковуємо дату та значення за індексом мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
print "At {} you could buy 1 IDR by {} CZK.".format(list_of_date[min_index], min(list_of_value))
