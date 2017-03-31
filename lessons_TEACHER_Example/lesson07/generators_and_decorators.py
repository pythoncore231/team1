# -*- coding: utf-8 -*-

# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
# print winning_lottery_numbers
# fake_lottery_numbers = [2*n for n in winning_lottery_numbers] 
# print fake_lottery_numbers
# fake_list_of_pair = [(i, j) for i in range(5) for j in range(10, 15)]
# print fake_list_of_pair
# fake_list_of_pair = [(i, j) for i in range(5) for j in range(10, 15) if i+j == 15]
# print fake_list_of_pair
# fake_list_of_pair = []

# print fake_list_of_pair
# for i in range(5):
#     for j in range(10, 15):
#         if i+j == 15:
#             fake_list_of_pair.append((i,j))
# print fake_list_of_pair

# fake_list_of_pair = {i:j for i in range(5) for j in range(10, 15) if i+j == 15}
# print fake_list_of_pair

# l1 = [1,2,3,4,5]
# l2 = ["a", "b", "c", "d", "e","e"]
# z = zip(l1,l2,l2)
# print z
# for i in z:
#     print i
# for a, b, c in z:
#     print a, b, c

# l = lambda a: a*a
# print type(l)
# print l(1)


# def isPos(number, lim = 1E-16):
#     return number > lim

# a = [-1,2,-3,4,-5,6,-7,8,-9,10]
# res = filter(isPos, a)
# print res
# res = filter(lambda i: not isPos(i), a)
# print res

# res = filter(lambda n: n> 1E-16, a)
# print res
# l = [1, 2]
# # l = ["1", "2", "3", "4", "5", "6", "7"]
# print [str(i) for i in l]
# t = map(lambda x: dict.fromkeys([x]), l)
# print t
# d1, d2 = t
# print d1, d2
# print dict.setdefault()
# def a_add_b(a, b):
#     r = a + b
#     print "a:{} b:{} r:{}".format(a, b, r)
#     return r

# print reduce(a_add_b, [47,11,42,13]) 
# print reduce(a_add_b, [47,11,42,5], 999) 
# print reduce(a_add_b, range(10)) 

# g = (i for i in range (10) if not i%2 )
# gt = [i for i in range (10) if not i%2 ]
# print g
# print gt
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# g = (i for i in range (10) if not i%2 )
# for i in g:
#     print i

# l = [i for i in range(999)]
# g = (i for i in range(999))
# print l.__sizeof__()
# print g.__sizeof__()

# def my_renge(n):
#     return range(n)
# l = my_renge(10)
# print l
# def my_xrange(n):
#     count = 1
#     while True:
#         print "start", count, n
#         if count < n:
#             yield count
#         else:
#             break
#         count += 1
#         print "end", count 

# g = my_xrange(10)
# print dir(g)

# print "\t\t {}".format(g.next())
# print "\t\t {}".format(g.next())
# for i in g:
#     if(i == 8):
#         g.close()
#     print i


# def my_func(n):
#     print type(n)
#     return n

# print my_func(2)
# print my_func(3)

# def f():
#     return 10

# print f()

# @my_func
# def f():
#     return 10

# print f()

# def retriy(f):
#     n = 0
#     while (n < 3)
#         try:
#             data = f()
#             return data
#         time.slip(3)
#         n += 1
#     return None


# def decorator(f):
#     print "This line is run once during func = decorator(func)"
#     def wrapper(*args, **kwargs):
#         print "This line is executed just before the function is called"
#         #Call the function
#         ret = f(*args, **kwargs)
#         print "This line is executed just after the function is called"
#         #Return the function's return  
#         return ret
#     return wrapper

# @decorator
# def foo(bar):
#     print bar 


# print
# foo("sss")


def decorator(f):
    number = f
    def wrapper(*args, **kwargs):
        # print "This line is executed just before the function is called"
        #Call the function
        ret = sum(args) + number
        # print "This line is executed just after the function is called"
        #Return the function's return  
        return ret
    return wrapper

t = decorator(5)
print t(10)
print t(*range(10))
t1 = decorator(50)
print t1(10), t(10)