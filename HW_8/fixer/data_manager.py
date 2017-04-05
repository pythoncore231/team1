# -*- coding: utf-8 -*-
import requests


def get_rates(date=None, base=None):
    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'
    if base:
        url = "{}?base={}".format(url, base)
    print url
    data = requests.get(url)
    data = data.json()
    return dict(data)


if __name__ == '__main__':
    pass
