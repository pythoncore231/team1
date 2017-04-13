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


def print_dict(obj):
    for i in obj:
        if isinstance(obj[i], dict):
            print "{}:".format(i)
            for j in obj[i]:
                print "\t{}: {}".format(j, obj[i][j])
        else:
            print "{}: {}".format(i, obj[i])


def min_dict(obj):
    l = []
    for i in obj:
        if isinstance(obj[i], dict):
            for j in obj[i]:
                l.append(obj[i][j])
    return min(l)


def max_dict(obj):
    l = []
    for i in obj:
        if isinstance(obj[i], dict):
            for j in obj[i]:
                l.append(obj[i][j])
    return max(l)

# def dict_in_list(obj):
#     l = []
#     for i in obj:
#         if isinstance(obj[i], dict):
#             for j in obj[i]:
#                 l.append(obj[i][j])
#     return l

data = get_rates_by_date()
print data
print_dict(data)
print "min: {}".format(min_dict(data))
print "max: {}".format(max_dict(data))

# print "min: {}".format(min(dict_in_list(room.in)))
# print "max: {}".format(max(dict_in_list(room.in)))