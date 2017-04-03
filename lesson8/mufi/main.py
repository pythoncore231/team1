

from fixer import data_manager

from utils import print_data

data = data_manager.get_rates_by_date()

print_data.print_dict(data)


print data_manager.get_rates_by_date("2012-03-03")



#print a
#print_dict(a)

# print_dict(obj)
# data = get_rates_by_date()
# print data
# print print_dict(data)
