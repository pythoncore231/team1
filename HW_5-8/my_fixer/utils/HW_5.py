# -*- coding: utf-8 -*-
import datetime
import requests


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
    print url


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


def get_rates_by_period(start_date, end_date, base=None):
    """
      generator

      :param start_date(str):
      :param end_date(str):
      :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                                 'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                                 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                                 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
      :return dict or None (if error):
      """

    start_date = map(int, start_date.split("-"))
    start_date = datetime.date(*start_date)

    end_date = map(int, end_date.split("-"))
    end_date = datetime.date(*end_date)

    while start_date <= end_date:
        date = str(start_date)
        date = get_rates(date, base)
        yield date
        start_date = start_date + datetime.timedelta(days=1)


if "__name__" == "__main__":

    date = get_rates_by_period("2012-03-10","2012-03-15")
    for i in date:
        print i
        print

