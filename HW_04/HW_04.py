# #-*- coding: utf-8 -*-
# #Prime numbers
# n=int(raw_input('Input number >=2:'))
# for i in range(2, n+1):
#     if n%i==0 and i!=n:
#         print 'It`s NOT a prime number.'
#         break
# else:
#     print 'It`s a PRIME number.'

# #Find 4-digit numbers sum one`s is equalent inputed number
# n=int(raw_input('Input number in range 1-36: '))
# for i in range(1000, 10000):
#     i=str(i)
#     if int(i[0])+int(i[1])+int(i[2])+int(i[3])==n:
#         print i

# #Fibonacci
# n=int(raw_input('Input number of order Fibonacci: '))
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a+b
#     print 'The number of Fibonacci is ', a 
# i===0???

# #The third degree
# n=int(raw_input('Input number: '))
# n=str(n)
# s=0
# for i in range(len(n)):
#     a=int(n[i])**3
#     s+=a
# print 'Sum is', s

# #Find text
# s1 ="""The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense."""

# print s1
# f=str(raw_input('Input templates: '))
# s1=s1.replace('\n', ' ')
# s1=s1.strip()
# s2=s1.split(' ')
# k=0

# for i in s2:
#     g=i.find(f)
#     if g==0:
#         k+=1
# print k
num = int(raw_input("num = "))
testNumbers = (2, 3, 5, 7)

for i in testNumbers:
    if not num == i and not num % i:
        result = False
        break
    else:
        result = True
print result