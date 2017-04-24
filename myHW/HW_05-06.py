# -*- coding: utf-8 -*-

import requests

def date_validation(date):
    if not isinstance(date, str):
        print "Введіть дату типу string"
        return False
    parts = date.split('-')
    if not len(parts) == 3:
        print "Дата не відповідає формату ""РРРР-ММ-ДД"""
        return False
    num = ('1','2','3','4','5','6','7','8','9','0')
    for part in parts:
        for i in part:
            if not i in num:
                print "Дата містить недозволені символи"
                return False
    year = int(parts[0])
    if year < 1999:
        print "Введено неправильний рік"
        return False
    month = int(parts[1])
    if not month in range(0,13):
        print "Помилка у введенні місяця"
        return False
    day =int(parts[2])
    leapyear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
    if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or month in (4, 6, 9, 11) and day <= 30 or leapyear and month ==2 and day <= 29 or not leapyear and month == 2 and day <=28):
        print "Введено неправильну дату"
        return False
    return True
def base_validation(base):

    bases = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBD', 'DKK', 'CAD', 'JPY', 'HF', 'RON', 'MYR', 'SEK' , 'SGD', 'HKD', 'AD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'USD')
    if not base in bases:
        print "Неправильна валюта"
        return False
    else:
        return True


def get_rates(date=None, base=None):
    """
    :param date(str or None): format "2000-01-03"
    :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
    :return dict or None (if error):
    """

    if date:
        if not date_validation(date):
            return
    if base:
        if not base_validation(base):
            return
    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)
    print url


    data = requests.get(url)
    data = data.json()
    return dict(data)


def print_dict_rates(obj):
    """
    :param obj(dict):
    :return None:
    """

    for i in obj:
        if isinstance(obj[i], dict):
            print "{}:".format(i)
            for j in obj[i]:
                print "\t{}: {}".format(j, obj[i][j])
            else:
                print "{}: {}".format(i,obj[i])
    pass

def exchange(amount, rates, to):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """

    if not base_validation(to):
        return
    if not isinstance(amount, int):
        print "Введено некоректну суму"
        return
    rate = rates.get('rates').get(to)
    if rate:
        return amount * rate
    pass

print_dict_rates(get_rates("2017-03-20", 'USD'))
print_dict_rates(get_rates("2017-03-21", 'USD'))
print_dict_rates(get_rates("2017-03-22", 'USD'))
print_dict_rates(get_rates("2017-03-23", 'USD'))
print_dict_rates(get_rates("2017-03-27", 'USD'))
print_dict_rates(get_rates("2017-03-24", 'USD'))
print_dict_rates(get_rates("2017-03-25", 'USD'))
print_dict_rates(get_rates("2017-03-26", 'USD'))

date = get_rates("2017-03-20", 'DKK')
print "100 DKK = {} BGN". format(exchange(100,date,'BGN'))
print "100 DKK = {} KRW". format(exchange(100,date,'KRW'))
