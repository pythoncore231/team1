# -*- coding: utf-8 -*-

import requests
from entity.currency import Currency 

def get_rates(date=None, base=None):
    """
    :param date(str or None): format "2000-01-03"
    :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
    :return dict or None (if error):
    """

    """ ToDo
        1) додати перевірку у випадку якщо `date` не None на коректність введення згідно формату
        2) додати перевірку у випадку якщо `base` не None на коректність введення,
           є конкретна множина допустимих значень

    """

    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)
    # print url


    data = requests.get(url)
    data = data.json()
    return dict(data)


def print_dict_rates(obj):
    """
    :param obj(dict):
    :return None:
    """

    """ ToDo
    додати реалізацію яка видруковує вхідний словник у вигдаді:
        date: 2017-03-27
        base: EUR
        rates
            USD: 1.0889
            IDR: 14486.0
        	BGN: 1.9558
        	...
    """

    pass

def exchange(amount, rates, to):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """

    """ ToDo
        функція приймає 3 параметри,
        `amount` - сума яку требе обміняти,
        `rates` - словник який повертає `get_rates()` для валюти з якиї ми збираємось обмінювати,
        `to` - абрівіатура валюти в яку необхідно обсміняти,
        повертає суму після обміну
    """
    pass


""" ToDo
   1) вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року
   2) вивести суму яку буде при обміня певної суми DKK на BGN та KRW
"""
# print get_rates()

# data = [Currency(**get_rates(date="2017-01-{}".format(i))) for i in range(10,15)]

data = []
for i in range(10,15):
    temp = get_rates(date="2017-01-{}".format(i))
    currency = Currency(date=temp["date"],
                        base=temp["base"],
                        rates=temp["rates"])
    data.append(currency)

print data

for i in data:
    print i

print data[0] - data[1]
print data[0] - 1

print data[0].sub(data[1])