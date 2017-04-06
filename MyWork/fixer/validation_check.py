# -*- coding: utf-8 -*-


def date_validations(date):
    """
    :param date(str):
    :return True or False (if error):
    """

    if not isinstance(date, str):
        print "Введена дата має бути типу string"
        return False

    parts = date.split('-')
    if not len(parts) == 3:
        print "Введена дата не відповідає формату ""РРРР-ДД-ММ"""
        return False

    num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for part in parts:
        for i in part:
            if not i in num:
                print "Введена дата містить недопустимі символи"
                return False

    year = int(parts[0])
    if year < 1999:
        print "Рік введено некоректно"
        return False

    month = int(parts[1])
    if not month in range(0, 13):
        print "Місяць введено некоректно"
        return False

    day = int(parts[2])
    leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
    if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
                                    month in (4, 6, 9, 11) and day <= 30 or \
                                    leapYear and month == 2 and day <= 29 or \
                                    not leapYear and month == 2 and day <= 28):
        print "День введено некоректно"
        return False

    return True


def base_validations(base):
    """
    :param base(str):
    :return True or False (if error):
    """

    bases = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
              'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
              'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
              'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'USD')

    if not base in bases:
        print "Валюта введена некоректно"
        return False
    else:
        return True
