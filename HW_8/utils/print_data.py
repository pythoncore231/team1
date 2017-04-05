# -*- coding: utf-8 -*-
def check_date(date):
    if date is None:
        return date
    elif isinstance(date, str):
        if not date[4] == date[7] == "-":
            print "Date is incorrect"
            return
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        leap = year % 400 == 0 or year % 4 == 0 and not (year % 100) == 0

        if year not in range(2000, 9999):
            print "Year is incorrect"
            return

        if month not in range(1, 13):
            print "Month is incorrect"
            return

        if day < 1 or day > 31:
            print "Day is incorrect"
            return

        elif month == 2:
            if leap and day > 29:
                print "Day is incorrect"
                return
            elif leap is False and day > 28:
                print "Day is incorrect"
                return

        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day > 31:
                print "Day is incorrect"
                return

        elif month in (4, 6, 9, 11):
            if day > 30:
                print "Day is incorrect"
                return
    return date


def check_base(base):
    list_base = ('EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW',
                 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RUB', 'INR', 'MXN',
                 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR')
    if base is None:
        return base
    if base not in list_base:
        print "Base is incorrect"
        return
    return base


# функція для отримання попереднього дня для формату дати "YYYY-MM-DD"
def yesterday(last_date):
    day = int(last_date[8:10])
    month = int(last_date[5:7])
    year = int(last_date[:4])
    leap = year % 400 == 0 or year % 4 == 0 and not (year % 100) == 0

    yes_ter_day = day - 1

    if yes_ter_day < 1:
        month -= 1
        if month < 1:
            month += 12
            year -= 1
        if month in (1, 3, 5, 7, 8, 10, 12):
            yes_ter_day += 31
        if month in (4, 6, 9, 11):
            yes_ter_day += 30
        if month == 2 and leap:
            yes_ter_day += 29
        if month == 2 and not leap:
            yes_ter_day += 28

        if len(str(month)) < 2:
            yes_ter_day_month = "0{}".format(month)
        else:
            yes_ter_day_month = "{}".format(month)
        if len(str(yes_ter_day)) < 2:
            yes_ter_day_day = "0{}".format(yes_ter_day)
        else:
            yes_ter_day_day = "{}".format(yes_ter_day)
        return "{}-{}-{}".format(year, yes_ter_day_month, yes_ter_day_day)
    else:
        if len(str(month)) < 2:
            yes_ter_day_month = "0{}".format(month)
        else:
            yes_ter_day_month = "{}".format(month)
        if len(str(yes_ter_day)) < 2:
            yes_ter_day_day = "0{}".format(yes_ter_day)
        else:
            yes_ter_day_day = "{}".format(yes_ter_day)
        return "{}-{}-{}".format(year, yes_ter_day_month, yes_ter_day_day)


# рекурсивна функція для діставання словників зі словників
def dict_rec(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            dict_rec(obj[each])
            return obj[each]


def print_dict(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            for every in obj[each]:
                print "\t{}: {}".format(every, obj[each][every])
        else:
            print "{}: {}".format(each, obj[each])


def print_3_days(dict_1, dict_2, dict_3):
    list_check = sorted(dict_rec(dict_1).keys())    # витягуємо ключики, створюємо з них сортований список
    for each in list_check:             # запускаємо цикл по списку назв валют
        val_1 = dict_rec(dict_1)[each]  # за назвою валюти дістаємо її курс на 1 дату
        val_2 = dict_rec(dict_2)[each]  # за назвою валюти дістаємо її курс на 2 дату
        val_3 = dict_rec(dict_3)[each]  # за назвою валюти дістаємо її курс на 3 дату
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_3


def last_3_days(list_dict):
    list_check = sorted(dict_rec(list_dict[0]).keys())
    for each in list_check:
        val_1 = dict_rec(list_dict[0])[each]
        val_2 = dict_rec(list_dict[1])[each]
        val_3 = dict_rec(list_dict[2])[each]
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_3


def print_difference(dict_1, dict_2):
    list_check = sorted(dict_rec(dict_1).keys())
    for each in list_check:             # запускаємо цикл по списку
        val_1 = dict_rec(dict_1)[each]  # за назвою валюти дістаємо її курс на 1 дату
        val_2 = dict_rec(dict_2)[each]  # за назвою валюти дістаємо її курс на 2 дату
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_2 - val_1


def print_exchange(amount, rates, to):
    result = float
    for each in rates:
        if isinstance(rates, dict):
            for every in rates[each]:
                if every == to:
                    result = amount * rates[each][every]
    return result


if __name__ == '__main__':
    pass
