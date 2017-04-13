'''
Created on Apr 5, 2017

@author: vodachuk
'''
# from utils.print_data import difference, exchange, Condition, print_dict_rates, yesterday, get_rates_by_period_from_to
from fixer.data_manager import get_rates, get_rates_by_period
from entity.currency import Currency

if __name__ == '__main__':
#     print difference("2017-03-30", "2017-04-03", "USD")
#     print exchange(10, "DKK", "BGN")
#     print exchange(10, "DKK", "KRW")
#     data = get_rates("2017-01-25")
#     print "\n", "Rate for the TRY on 2017-01-25"
#     Condition(data, "TRY")
#     date = get_rates(base = "USD")
# 
#     print_dict_rates(date)
#     data = [i for i in get_rates_by_period_from_to("2013-01-01", "2013-01-25", 'IDR', 'CZK')]
#     print "min = {}".format(min(data))
#     
#     
#     date_basis = "2013-01-"
#     list_of_date = ["{}{}{}".format(date_basis, 0, i) if len(str(i)) < 2
#                 else "{}{}".format(date_basis, i) for i in range(1, 26)]
# 
# 
#     list_of_value = [exchange(1, 'IDR', 'CZK')for j in list_of_date]
# 
# 
#     min_index = list_of_value.index(min(list_of_value))
# 
#     
#     print "At {} you could buy 1 IDR by {} CZK.".format(list_of_date[min_index], min(list_of_value))\
    print '{:*^50}'.format("print rates in one day")
    currency = Currency(**get_rates("2017-01-25", 'TRY'))
    print currency
    ### exchange
    print '\n{:*^50}'.format("print exchange")
    currency = Currency(**get_rates("2017-03-27", 'DKK'))
    print currency.exchange(100, 'BGN')

    ### difference
    print '\n{:*^50}'.format("print difference")
    data = [Currency(**rate) for rate in get_rates_by_period("2017-03-20", "2017-03-27", 'USD')]
    print data[0].difference(data[2])
    print data[0].difference(*data)
#     data = []
#     for i in range(10,15):
#         temp = get_rates(date="2017-01-{}".format(i))
#         currency = Currency(date=temp["date"],
#                             base=temp["base"],
#                             rates=temp["rates"])
#         data.append(currency)
# 
#     print data
# 
#     for i in data:
#         print i
# 
#     print data[0] - data[1]
    
    
    