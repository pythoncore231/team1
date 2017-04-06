# -*- coding: utf-8 -*-

from fixer.data_manager import get_rates, get_rates_by_period, get_rates_by_period_from_to
from utils.print_data import print_dict_rates, print_dict_rates_by_period, exchange

print "1"
print_dict_rates_by_period(get_rates_by_period("2017-04-01", "2017-04-03", 'USD'))

print "2"
print_dict_rates(get_rates("2017-01-25", 'TRY'))

print "3"
data = [i for i in get_rates_by_period_from_to("2013-01-01", "2013-01-25", 'IDR', 'CZK')]
print "min = {}".format(min(data))