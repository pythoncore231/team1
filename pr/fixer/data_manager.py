import requests

def get_rates(date=None, base=None):
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

def get_rates_by_period(date_1, date_2, base=None):
    if not date_validator(date_1) and  not date_validator(date_2) and not base_validator(base):
        return False
    else:
        rates_by_dates=()
        for i in range (10, 15):
            get_rates('2017-04-{}'.format(i), base)
            rates_by_dates.append()

def date_validator(date):
    if not isinstance(date, str):
        print "Input in format of string"
        return False
    parts = date.split('-')
    if not len(parts) == 3:
        print "Input date in format YYYY-DD-MM"
        return False
    num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for part in parts:
        for i in part:
            if not i in num:
                print "Only digits should be contained"
                return False
    year = int(parts[0])
    if year < 1999:
        print "Input year after 1999"
        return False
    month = int(parts[1])
    if not month in range(0, 12):
        print "Month is incorrect"
        return False
    day = int(parts[2])
    leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
    if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
                                    month in (4, 6, 9, 11) and day <= 30 or \
                                    leapYear and month == 2 and day <= 29 or \
                                    not leapYear and month == 2 and day <= 28):
        print "Day is incorrect"
        return False

    return True

def base_validator(base):
    bases = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
              'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
              'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
              'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'USD')
    if not base in bases:
        print "Base is incorrect"
        return False
    else:
        return True