# def my_func():
#     my_temp = 1
#     print "begin"
#     my_temp += 1
#     return "foo"
#     print "end"

# print my_func()
# print my_func(1)
# def my_func(val):
#     if isinstance(val, list):
#         val.append(1)
#     elif isinstance(val, tuple):
#         val = val + (1,)
#     return val

# l = [1,2,3,4,5]
# t = (1,2,3,4,5)

# print l
# print my_func(l)
# print l
# print t
# print my_func(t)
# print t


# def my_func(a, b=1, c = None):
#     return "a:{} b:{} c:{} ".format(a, b, c)

# print my_func(1, 2)
# print my_func(2, 1)
# print my_func(b=1, a=2)
# print my_func(1,2,3)
# print my_func(a=1, c=2)

# def my_func(a, b=None, *t, **d):
#     return "a:{} b:{} t:{} d:{}".format(a, b, t, d)

# print my_func(1, 2)
# print my_func(2, 1)
# print my_func(b=1, a=2)
# print my_func(1,2,3)
# print my_func(a=1, c=2)
# print my_func(1,2,3,4,5,6, f=1, g=1)
# my_tuple = (1,2,3,4)
# print my_func(my_tuple)
# print my_func(*my_tuple)
# my_dict = {"a":1, "b":2, "c":3}
# print my_func(my_dict)
# print my_func(*my_dict)
# print my_func(**my_dict)

# my_f = lambda a, b, c: a+b+c
# print my_f(1,2,3)

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
    # Todo 

data = get_rates_by_date()
print data
print print_dict(data)