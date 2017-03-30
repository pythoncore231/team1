# -*- coding: utf-8 -*-
import requests


def check_date(date):
    if isinstance(date, str):
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        leap = year % 400 == 0 or year % 4 == 0 and not (year % 100) == 0

        if year not in range(2000, 9999):
            print u"Year is incorrect"

        if month not in range(1, 13):
            print u"Month is incorrect"

        if day < 1 or day > 31:
            print u"Day is incorrect"

        elif month == 2:
            if leap and day > 29:
                print u"Day is incorrect"
            elif leap is False and day > 28:
                print u"Day is incorrect"

        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day > 31:
                print u"Day is incorrect"

        elif month in (4, 6, 9, 11):
            if day > 30:
                print u"Day is incorrect"

    return date


def check_base(base):
    list_base = (u'EUR', u'USD', u'IDR', u'BGN', u'ILS', u'GBP', u'DKK', u'CAD', u'JPY',
                 u'HF', u'RON', u'MYR', u'SEK', u'SGD', u'HKD', u'AD', u'CHF', u'KRW',
                 u'CNY', u'TRY', u'HRK', u'NZD', u'THB', u'NOK', u'RB', u'INR', u'MXN',
                 u'CZK', u'BRL', u'PLN', u'PHP', u'ZAR')
    if base not in list_base:
        print u"Base is incorrect"
    return base


def print_dict(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            for every in obj[each]:
                print u"\t{}: {}".format(every, obj[each][every])
        else:
            print obj[each]


def get_rates(date=None, base=None):
    if date is not None:
        check_date(date)
    if base is not None:
        check_base(base)
    url = u"http://api.fixer.io/"
    if date:
        url += date
    else:
        url += u'latest'
    if base:
        url = u"{}?base={}".format(url, base)
    print url
    data = requests.get(url)
    data = data.json()
    return dict(data)


def exchange(amount, rates, to):
    rates_dict = get_rates(None, rates)
    result = float
    for each in rates_dict:
        if isinstance(rates_dict, dict):
            for every in rates_dict[each]:
                if every == to:
                    result = amount * rates_dict[each][every]
    return u"{} {} is {} {}".format(amount, rates, result, to)


def period(date_1, date_2, base):
    day_1 = int(date_1[8:10])
    day_2 = int(date_2[8:10])
    for i in range(day_1, day_2+1):
        date = date_1[:8]+u"{}".format(i)
        a = get_rates(date, base)
        print print_dict(a)

print period(u"2017-03-20", u"2017-03-27", u"USD")
print exchange(10, u"DKK", u"BGN")
print exchange(10, u"DKK", u"KRW")
