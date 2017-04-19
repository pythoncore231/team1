from fixer.data_manager import get_rates

def print_dict_rates(obj):
    for i in obj:
        if isinstance(obj[i], dict):
            print '{}:'.format(i)
            for n in obj[i]:
                print '\t{}: {}'.format(n, obj[i][n])
        else:
            print '{}: {}'.format(i, obj[i])

def max(obj):
    l = []
    for i in obj:
        if isinstance(obj[i], dict):
            for n in obj[i]:
                l.append(obj[i][n])
    return max(l)

def min(obj):
    l = []
    for i in obj:
        if isinstance(obj[i], dict):
            for n in obj[i]:
                l.append(obj[i][n])
    return min(l)

def exchange(amount, rates, to):
    rates = get_rates(None, rates)
    for i in rates:
        if isinstance(rates, dict):
            for n in rates[i]:
                if n == to:
                    res = float(amount * rates[i][n])
                    return res
                else:
                    print 'Incorrect currency'