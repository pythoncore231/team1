'''
Created on Apr 5, 2017

@author: vodachuk
'''
from utils.print_data import difference, exchange, Condition, print_dict_rates, yesterday, get_rates_by_period_from_to
from fixer.data_manager import get_rates

if __name__ == '__main__':
#     print difference("2017-03-30", "2017-04-03", "USD")
#     print exchange(10, "DKK", "BGN")
#     print exchange(10, "DKK", "KRW")
#     Condition(data)
    data = get_rates("2017-01-25")
    print "\n", "Rate for the TRY on 2017-01-25"
    Condition(data, "TRY")
#     date = get_rates(base = "USD")["date"]

    data = [i for i in get_rates_by_period_from_to("2013-01-01", "2013-01-25", 'IDR', 'CZK')]
    print "min = {}".format(min(data))
    