# -*- coding: utf-8 -*-
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
    print
    print " ", "Base:", "\t ", list_dict[0]["date"], "\t ", list_dict[1]["date"], "\t ", list_dict[2]["date"]
    print
    list_check = sorted(dict_rec(list_dict[0]).keys())
    for each in list_check:
        val_1 = dict_rec(list_dict[0])[each]
        val_2 = dict_rec(list_dict[1])[each]
        val_3 = dict_rec(list_dict[2])[each]
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_3


def last_n_days(list_of_rates):
    header = " {}: \t".format('Base')
    for d in list_of_rates:
        header += "{} \t".format(d['date'])
    print
    print header
    print
    list_of_dict = [dict_rec(i) for i in list_of_rates]
    list_of_names = sorted(list_of_dict[0])
    for base_names in list_of_names:
        some = [t_2 for t_2 in [value[base_names] for value in list_of_dict]]
        line = " {}: \t".format(base_names)
        for every in some:
            if len(str(every)) < 4:
                line += "{}\t\t\t".format(every)
            else:
                line += "{}\t\t".format(every)
        print line


def print_difference(dict_1, dict_2):
    list_check = sorted(dict_rec(dict_1).keys())
    for each in list_check:             # запускаємо цикл по списку
        val_1 = dict_rec(dict_1)[each]  # за назвою валюти дістаємо її курс на 1 дату
        val_2 = dict_rec(dict_2)[each]  # за назвою валюти дістаємо її курс на 2 дату
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_2 - val_1


def exchange(amount, rates, to):
    for each in rates:
        if isinstance(rates, dict):
            for every in rates[each]:
                if every == to:
                    return amount * rates[each][every]


if __name__ == '__main__':
    pass
