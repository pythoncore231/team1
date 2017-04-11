# -*- coding: utf-8 -*-
import requests


def check_date_base(date=None, base=None):
    if date is None:
        return True
    elif isinstance(date, str):
        if not date[4] == date[7] == "-":
            print "Date is incorrect"
            return False
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        leap = year % 400 == 0 or year % 4 == 0 and not (year % 100) == 0

        if year not in range(2000, 9999):
            print "Year is incorrect"
            return False

        if month not in range(1, 13):
            print "Month is incorrect"
            return False

        if day < 1 or day > 31:
            print "Day is incorrect"
            return False

        elif month == 2:
            if leap and day > 29:
                print "Day is incorrect"
                return False
            elif leap is False and day > 28:
                print "Day is incorrect"
                return False

        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day > 31:
                print "Day is incorrect"
                return False

        elif month in (4, 6, 9, 11):
            if day > 30:
                print "Day is incorrect"
                return False

    list_base = ('EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW',
                 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RUB', 'INR', 'MXN',
                 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR')
    if base is None:
        return True
    if base not in list_base:
        print "Base is incorrect"
        return False

    return True


def get_rates(date=None, base=None):
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


def checked_rates(date=None, base=None):
    if check_date_base(date, base):
        return get_rates(date, base)
    else:
        print "Either date or base are invalid."


def dict_rec(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            dict_rec(obj[each])
            return obj[each]


def print_dict(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            for every in obj[each]:
                print u"\t{}: {}".format(every, obj[each][every])
        else:
            print obj[each]


def exchange(amount, rates, to):
    for each in rates:
        if isinstance(rates, dict):
            for every in rates[each]:
                if every == to:
                    return amount * rates[each][to]


def print_difference(dict_1, dict_2):
    list_check = sorted(dict_rec(dict_1).keys())
    for each in list_check:             # запускаємо цикл по списку
        val_1 = dict_rec(dict_1)[each]  # за назвою валюти дістаємо її курс на 1 дату
        val_2 = dict_rec(dict_2)[each]  # за назвою валюти дістаємо її курс на 2 дату
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_2 - val_1


start_date_dict = checked_rates("2017-03-20", "USD")
end_date_dict = checked_rates("2017-03-27", "USD")

print_difference(start_date_dict, end_date_dict)

dkk = checked_rates(None, "DKK")
print exchange(10, dkk, "BGN")
print exchange(10, dkk, "KRW")
