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

    # def min_value(self, to, *data):
    #     # if not base_validator(to):
    #     #     return
    #     temp_min=[]
    #     for rates in data:
    #         temp_min.append(rates([to]), data(date))
    #     return min(temp_min)
    #     print temp_min 

    def day_of_min_rate(self, to, data):
        # if not base_validator(to):
        #     return
        # if not isinstance(data, tuple):
        #     return
        # for i in data:
            # if not isinstance(i, Currency):
            #     return
        rates = [(rate.rates[to], rate.date) for rate in data]
        print rates, type(rates)
        minValue = min(rates, key=lambda n: n[0])
        return "{}: {}".format(minValue[1], minValue[0])