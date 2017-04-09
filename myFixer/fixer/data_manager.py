# -*- coding: utf-8 -*-

import requests, datetime, validation_check as v


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
        if not v.date_validations(date):
            return

    if base:
        if not v.base_validations(base):
            return

    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)
    # print url

    data = requests.get(url)
    data = data.json()
    return dict(data)


def get_rates_by_period(start_date, end_date, base=None):
    """
    :param start_date(str):
    :param end_date(str):
    :param base(str):
    :return generator:
    """

    start_date = map(int, start_date.split("-"))
    start_date = datetime.date(*start_date)

    end_date = map(int, end_date.split("-"))
    end_date = datetime.date(*end_date)

    if start_date > end_date:
        return

    while start_date <= end_date:
        date = str(start_date)
        data = get_rates(date, base)
        yield data
        start_date = start_date + datetime.timedelta(days=1)