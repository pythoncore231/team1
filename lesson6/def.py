import requests


def get_rates_by_date(date=None):
    url = "http://api.fixer.io/"
    if date:
        url += date
    else:
        url += 'latest'
    data = requests.get(url)
    data = data.json()

    return data


#print get_rates_by_date()


#def print_dict(obj):
#    for i in obj:
#        if i == "date":
#            print i, obj[i]
#            for j in obj[i]:
#                print j, obj[i][j]


def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict): # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{}: {}".format(j,  obj[key][j])
        else:
             print "{}:{}".format(key, obj[key])


a = get_rates_by_date("2009-03-03")
print a
print_dict(a)

# print_dict(obj)
# data = get_rates_by_date()
# print data
# print print_dict(data)
