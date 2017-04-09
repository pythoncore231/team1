from fixer.data_manager import get_rates, get_rates_by_period
from entity.currency import Currency

### print
print '{:*^50}'.format("print rates in one day")
currency = Currency(**get_rates("2017-01-25", 'TRY'))
print currency

### print by period
print '\n{:*^50}'.format("print rates by period")
data = [Currency(**rate) for rate in get_rates_by_period("2017-04-01", "2017-04-10", 'USD')]
print data
print data[0].print_in_cols(*data)

### exchange
print '\n{:*^50}'.format("print exchange")
currency = Currency(**get_rates("2017-03-27", 'DKK'))
print currency.exchange(100, 'BGN')

### difference
print '\n{:*^50}'.format("print difference")
data = [Currency(**rate) for rate in get_rates_by_period("2017-03-20", "2017-03-27", 'USD')]
print data[0].difference(data[2])
print data[0].difference(*data)

### day of min exchange rate from x to y
print '\n{:*^50}'.format("print day of min exchange rate")
data = [Currency(**rate) for rate in get_rates_by_period("2013-01-01", "2013-01-25", 'IDR')]
print data[0].day_of_min_rate('CZK', *data)