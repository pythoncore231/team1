'''
Created on Mar 20, 2017
@author: vodachuk
'''
# a)
# import math *
from math import *
# e = 1E-5
# a = 0.05
# b = 0.9
# h = 0.1
# template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# print "-"*65
# x = a
# while x < b:
#     k = 1
#     s = k*(k + 1)*x**k
#     S = s
#     while s > e:
#         k += 1
#         s = k*(k+1)*x**k
#         S += s
#     y = 2*x/((1-x)**3)
#     p = fabs(((S-y)/y))*100
#     print template.format(x, S, y, p)
#     x += h
# print "-"*65

# b)

# e = 1E-5
# a = 0.1
# b = 0.9
# h = 0.1
# template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# print "-"*65
# x = a
# while x < b:
#     k = 0
#     s = (x ** (k - 2.)) / (factorial(k) * (k + 2.))
#     S = s
#     while s > e:
#         k += 1
#         s = (1. / (factorial(k) * (k + 2.))) * (x ** (k - 2.))
#         S += s
#     y = float(((x - 1.) * exp(x)) + 1.)    
#     p = fabs(((S-y)/y))*100
#     print template.format(x, S, y, p)
#     x += h
# print "-"*65

# c)
# e = 1E-5
# a = 0.1
# b = 0.9
# h = 0.1
# template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# print "-"*65
# x = a
# while x < b:
#     k = 1
#     s = k * (k + 2) * (x ** k)
#     S = s
#     while s > e:
#         k += 1
#         s = k * (k + 2) * (x ** k)
#         S += s
#     y = ( x * (3 - x) ) / ( (1 - x) ** 3 )   
#     p = fabs(((S-y)/y))*100
#     print template.format(x, S, y, p)
#     x += h
# print "-"*65

# d) ???????????? 
e = 1E-5
a = 0.1
b = 0.9
h = 0.1
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "-"*65
x = a
while x < b:
    k = 1
    m_1 = ( 2. * k + 3. )
    m_2 = 2. * k
    s = ( long(m_1) / long(m_2) ) * (x ** k)
    M_1 = m_1
    M_2 = m_2
    S = 1 - s
    while s > e:
        k += 1
        s = ( float(M_1) / float(M_2) ) * (x ** k)
        M_1 *= m_1
        M_2 *= m_2
        S += float(((-1.) ** k) * s)
    y = ( 1. + x ) ** (- 5. / 2)   
    p = fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65

# e)
# e = 1E-5
# a = 0.1
# b = 0.9
# h = 0.1
# template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# print "-"*65
# x = a
# while x < b:
#     k = 0
#     s = (2 * k + 1) * ( x ** k)
#     S = s
#     while s > e:
#         k += 1
#         s = (2 * k + 1) * ( x ** k)
#         S += s
#     y = (1 + x) / ((1 - x) ** 2)
#     p = fabs(((S-y)/y))*100
#     print template.format(x, S, y, p)
#     x += h
# print "-"*65