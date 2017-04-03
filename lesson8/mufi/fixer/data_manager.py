
import requests

def get_rates_by_date(date=None):
    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'
    data = requests.get(url)
    data = data.json()

    return data
