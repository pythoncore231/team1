import requests
from Course import date_validations


def date_validations(date):
    """
    :param date(str):
    :return True or False (if error):
    """

    if not isinstance(date, str):
        print "Input date must be type string"
        return False

    parts = date.split('-')
    if not len(parts) == 3:
        print "Entered date must have format YYYY-DD-MM"
        return False

    num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for part in parts:
        for i in part:
            if not i in num:
                print "Entered date include incorrect symbols"
                return False

    year = int(parts[0])
    if year < 1999:
        print "Incorrect year input"
        return False

    month = int(parts[1])
    if not month in range(0, 12):
        print "Incorrect month input"
        return False

    day = int(parts[2])
    leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
    if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
                                    month in (4, 6, 9, 11) and day <= 30 or \
                                    leapYear and month == 2 and day <= 29 or \
                                    not leapYear and month == 2 and day <= 28):
        print "Incorrect day input"
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
        print "Incorrect valute input"
        return False
    else:
        return True



def get_rates(date=None, base=None):
    """
    :param date(str or None): format "2000-01-03"
    :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'USD'}
    :return dict or None (if error):
    """

    if date:
        if not date_validations(date):
            return

    if base:
        if not base_validations(base):
            return

    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)

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
            print "{}: {}".format(i, obj[i])

    pass
def print_dict(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            for every in obj[each]:
                print u"\t{}: {}".format(every, obj[each][every])
        else:
            print obj[each]



def exchange(amount, rates, to):
    rates_dict = get_rates(None, rates)
    result = float
    for each in rates_dict:
        if isinstance(rates_dict, dict):
            for every in rates_dict[each]:
                if every == to:
                    result = amount * rates_dict[each][every]
    return u"{} {} is {} {}".format(amount, rates, result, to)


def dict_rec(obj):
    for each in obj:
        if isinstance(obj[each], dict):
            dict_rec(obj[each])
            return obj[each]



def difference(date_1, date_2, base):
    date_validations(date_1)
    date_validations(date_2)
    dict_1 = get_rates(date_1, base)
    dict_2 = get_rates(date_2, base)
    list_check = sorted(dict_rec(dict_1).keys())
    print
    print "Currency", "\t", date_1, "\t   ", date_2, "\t"*2, "Difference"
    print
    for each in list_check:
        val_1 = dict_rec(dict_1)[each]
        val_2 = dict_rec(dict_2)[each]
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_2 - val_1


print difference("2017-03-20", "2017-03-27", "USD")
print exchange(10, "DKK", "BGN")
print exchange(10, "DKK", "KRW")
