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

def get_rates_by_period(date_1=None, date_2=None, base=None):
    if not date_validator(date_1) and  not date_validator(date_2) and not base_validator(base):
        return False
    else:
        rates_by_dates=[]
        for i in range (20, 25):
            rates_by_dates.append(get_rates('2017-03-{}'.format(i), base))
        return rates_by_dates

def date_validator(date):
    
    if not isinstance(date, str) or not len(date.split('-')) == 3:
        print "Input in format of string and in format YYYY-DD-MM"
        return False

    parts = date.split('-')

    digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')  ### another way???
    for part in parts:
        for i in part:
            if not i in digits:
                print 'Only digits'
                return False

    year = int(parts[0])
    if year < 1999:
        print "Input year after 1999 and in digits"
        return False

    month = int(parts[2])
    if not 1 <= month <=12:
        print "Month is incorrect, or month is not digits"
        return False

    day = int(parts[1])
    if 1<=day<=28 and month==2 or day==29 and month==2 and year%4==0:
        return True
    elif 1<=day<=30 and month in (4, 6, 9, 11)  or  1<=day<=31 and month!=2:
        return True
    else:
        print 'Incorrect format of date'

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


print date_validator('2007-31-04')