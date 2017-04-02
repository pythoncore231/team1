# -*- coding: utf-8 -*-
# "2000-01-03"
import requests
def check_date(date):
    a = u"Date is incorrect"
    if isinstance(date, str):
        if not date[4] == date[7] == "-":
            print a
            return a
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        leap = year % 400 == 0 or year % 4 == 0 and not (year % 100) == 0

        if year not in range(2000, 9999):
            print u"Year is incorrect"
            return

        if month not in range(1, 13):
            print u"Month is incorrect"
            return

        if day < 1 or day > 31:
            print u"Day is incorrect"
            return

        elif month == 2:
            if leap and day > 29:
                print u"Day is incorrect"
                return
            elif leap is False and day > 28:
                print u"Day is incorrect"
                return

        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day > 31:
                print u"Day is incorrect"
                return

        elif month in (4, 6, 9, 11):
            if day > 30:
                print u"Day is incorrect"
                return

    return date

# base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
#                                'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
#                                'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
#                                'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}



def check_base(base):
    list_base = (u'EUR', u'USD', u'IDR', u'BGN', u'ILS', u'GBP', u'DKK', u'CAD', u'JPY',
                 u'HF', u'RON', u'MYR', u'SEK', u'SGD', u'HKD', u'AD', u'CHF', u'KRW',
                 u'CNY', u'TRY', u'HRK', u'NZD', u'THB', u'NOK', u'RB', u'INR', u'MXN',
                 u'CZK', u'BRL', u'PLN', u'PHP', u'ZAR')
    if base not in list_base:
        return False
    return base


# Функція для гарного вивода на екран начинки словника, подивитись як ымпортувати файли в ынший файл(фром реквест ымпорт гет)
def print_dict(obj):
    for each in obj:                        # запускаєм цикл
        if isinstance(obj[each], dict):     # який перевіряє, чи є значення заданного словника словником
            for every in obj[each]:         # якщо є, запускаєм новий цикл
                print u"\t{}: {}".format(every, obj[each][every])   # який роздруковує ключ і значення словника
        else:
            print obj[each]                 # якщо ні, виводить значення


# Функція, яка за датою та абривіатурою валюти відкриває необхідну лінку, та бере з неї словник з курсами валют
def get_rates(date=None, base=None):
    if date is not None:                # перевірка коректності введеної дати. Працює неправильно
        check_date(date)
    if base is not None:                # перевірка коректності введеної валюти. Працює неправильно
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
    print "123213==============================================================="
    print data
    data = data.json()
    return dict(data)


# функція, що обчислює обмін валют. Вбиваєм суму валют, абревіатуру валюти, яку міняєм, і на яку міняєм
def exchange(amount, rates, to):
    rates_dict = get_rates(None, rates)     # за назвою валюти, яку міняєм, знаходимо словник з курсами на останню дату
    result = float
    for each in rates_dict:
        if isinstance(rates_dict, dict):    # якщо словник
            for every in rates_dict[each]:  # запускаєм цикл по словнику
                if every == to:             # якщо ключ співпадає з назвою валюти, на яку міняєм
                    result = amount * rates_dict[each][every]   # помножуєм кількість на значення цієї валюти
    return u"{} {} is {} {}".format(amount, rates, result, to)  # гарно видруковуєм результат


# функція, що перевіряє, чи є в словнику інші словники, і вивертає їх пари ключ:значення. Те, що мені показав викладач
def dict_rec(obj):                          # беремо об'єкт
    for each in obj:                        # запускаємо в ньому цикл
        if isinstance(obj[each], dict):     # якщо елемент словника є словником
            dict_rec(obj[each])             # застосовуємо до нього цю ж функцію, доки не знайде усі словники
            return obj[each]                # для кожного словника вивертає пари ключ:значення


# функція, що розраховує різницю між курсами за двома датами, та назвою валюти
def difference(date_1, date_2, base):
    check_date(date_1)                  # перевірка коректності введеної дати. Працює неправильно
    check_date(date_2)                  # перевірка коректності введеної дати. Працює неправильно
    dict_1 = get_rates(date_1, base)    # дістаємо словник з курсами валют для 1 дати
    dict_2 = get_rates(date_2, base)    # дістаємо словник з курсами валют для 2 дати
    list_check = sorted(dict_rec(dict_1).keys())
    print   # ^ із 1 словника беремо назви валют(ключи), сортуємо за алфавітом, та упаковуємо у список
    print "Currency", "\t", date_1, "\t   ", date_2, "\t"*2, "Difference"
    print   # видруковуємо гарну шапку для таблиці
    for each in list_check:             # запускаємо цикл по списку
        val_1 = dict_rec(dict_1)[each]  # за назвою валюти дістаємо її курс на 1 дату
        val_2 = dict_rec(dict_2)[each]  # за назвою валюти дістаємо її курс на 2 дату
        print " ", each + ":", "\t "*2, val_1, "\t "*2, val_2, "\t "*2, val_2 - val_1
        # видруковуємо построково назву валюти, курс на 1 дату, курс на 2 дату, різницю курсів

print difference(u"2017-03-20", u"2017-03-27", u"USD")
print exchange(10, u"DKK", u"BGN")
print exchange(10, u"DKK", u"KRW")
