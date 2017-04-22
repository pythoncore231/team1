import requests
import sys

from entity.currency import Currency
from fixer.data_manager import get_rates, date_validator, base_validator, get_rates_by_period
from utils.print_data import print_dict_rates, max, min

# #Print rates of latest date
# print get_rates()

# #Print exchange 10.00  USD in EUR on 10th April 2017
# ex = Currency(**(get_rates('2017-04-10', 'USD'))).exchange(10, 'EUR')
# print ex

#Get currency rates of period 2017-01-10/14 in dict and object
# data = [Currency(**get_rates(date="2017-01-{}".format(i))) for i in range(10,14)]
# print data

# data = []
# for i in range(10,15):
#     temp = get_rates(date="2017-01-{}".format(i))
#     currency = Currency(date=temp["date"],
#                         base=temp["base"],
#                         rates=temp["rates"])
#     data.append(currency)

# print data


# print data[0] - data[1] ##difference between two dates __sub__: data[0] and data[2] from range (10, 14) 
# print data[0].sub(data[2]) #equalent difference by def 'sub'

# Date of min rate
# data = [Currency(**rate) for rate in get_rates_by_period('2017-01-10', '2017-01-30', 'USD')]
# print data[0].min_value('PLN', *data)

#Day of min exchange rate
data = [Currency(**get_rates(date="2017-03-{}".format(i))) for i in range(20,26)]
# data = [Currency(**rate) for rate in get_rates_by_period("2013-03-20", "2013-03-25", 'EUR')]
print data, type(data)
for i in data:
    print i, type (i)
print data[0].day_of_min_rate('PLN', data)