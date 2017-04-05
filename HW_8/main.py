# -*- coding: utf-8 -*-
from fixer.data_manager import get_rates
from utils.print_data import check_date, check_base, yesterday, print_dict, last_3_days, print_3_days, \
    print_difference, print_exchange

# DONE
# вивести різницю курсу валют для USD на 20 та 27 березня 2017 року
print
print "difference"
date_difference1 = get_rates(check_date("2017-03-20"), check_base("USD"))
date_difference2 = get_rates(check_date("2017-03-27"), check_base("USD"))


print_difference(date_difference1, date_difference2)

# DONE
# вивести суму, яку отримаєм при обміні певної суми DKK на BGN та KRW
print
print "exchange"
dkk = get_rates(check_date(None), check_base("DKK"))
print print_exchange(1, dkk, check_base("BGN"))
print print_exchange(1, dkk, check_base("KRW"))

# DONE
# вивести зміну курсу за 3 останні дні для USD
print
print "3_days"
day_1 = get_rates(check_date("2017-04-02"), check_base("USD"))
day_2 = get_rates(check_date("2017-04-03"), check_base("USD"))
day_3 = get_rates(check_date(None), check_base("USD"))


print_3_days(day_1, day_2, day_3)

# альтернативний варіант без вводу дати
print
print "last_3_days"
last_date = get_rates(None, check_base("USD"))["date"]  # із словника беремо запис останньої дати
list_3_days = [yesterday(yesterday(last_date)), yesterday(last_date), last_date]
list_dict = []
for date in list_3_days:
    list_dict.append(get_rates(date, check_base("USD")))

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
# створюємо список дат з 1/01/2013 по 25/01/2013
list_of_date = []
date = "2013-01-"
for i in range(1, 26):
    if len(str(i)) < 2:
        list_of_date.append("{}{}{}".format(date, 0, i))
    else:
        list_of_date.append("{}{}".format(date, i))

# створюємо список значень курсу CZK для IDR з 1/01/2013 по 25/01/2013
list_of_value = []
for j in list_of_date:
    rates = get_rates(check_date(j), check_base('IDR'))
    from_IDR_to_CZK = print_exchange(1, rates, check_base('CZK'))
    list_of_value.append(from_IDR_to_CZK)
# визначаємо індекс мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
min_index = list_of_value.index(min(list_of_value))
# роздруковуємо дату та значення за індексом мінімального значення курсу CZK для IDR з 1/01/2013 по 25/01/2013
print "At {} you could buy 1 IDR by {} CZK.".format(list_of_date[min_index], min(list_of_value))
