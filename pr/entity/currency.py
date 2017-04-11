import sys
sys.path.append('C:\\users\\angelo\\desktop\\Python\\project\\team1\\pr')
from fixer.data_manager import get_rates, get_rates_by_period, date_validator, base_validator

class Currency(object):

    def __init__(self, date, base, rates):
        self.date = date
        self.base = base
        self.rates = rates

    def __repr__(self):
        return "<{} {}>".format(self.base, self.date)

    def __str__(self):
        template = "{} {}\n".format(self.base, self.date)
        for key in self.rates:
            template += "{}: {}, ".format(key, self.rates[key])
        return template

    def __sub__(self, other):
        result = {}
        for key in self.rates:
            result[key] = self.rates[key] - other.rates[key]
        return result

    def sub(self, other): #difference between two dates
        result = {}
        for key in self.rates:
            result[key] = self.rates[key] - other.rates[key]
        return result

    def exchange(self, amount, to):
        if not isinstance(amount, (float, int)):
            return
        if not base_validator(to):
            return
        else:
            return '{} {} is {} {}'.format(amount, self.base, amount * self.rates[to], to)

    # def day_of_min(self, date, base, rates):