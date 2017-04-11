import requests
import sys

from entity.currency import Currency
from fixer.data_manager import get_rates, date_validator, base_validator
from utils.print_data import print_dict_rates, max, min

#Print rates of latest date
# print get_rates()

#Print exchange 10.00  USD in EUR on 10th April 2017
# ex = Currency(**(get_rates('2017-04-10', 'USD'))).exchange(10, 'EUR')
# print ex

data = [Currency(**get_rates(date="2017-01-{}".format(i))) for i in range(10,15)]
print data

# data = []
# for i in range(10,15):
#     temp = get_rates(date="2017-01-{}".format(i))
#     currency = Currency(date=temp["date"],
#                         base=temp["base"],
#                         rates=temp["rates"])
#     data.append(currency)

# # print data

# # for i in data:
# #     print i

# # print data[0] - data[2] ##difference between two dates: data[0] and data[2] from range (10, 15) 
# # print data[0].sub(data[1]) #equalent difference

