# a=int(raw_input("Number: "))
# if a>1:
#     for i in range(2,a):
#         if (a%i)==0:
#             print(a,i,"It's not a prime number")
#             continue
#         else: print (a,i,"It's a prime number")
# else: print (a,"It's not a prime number")
#
# a=int(raw_input("Enter number:"))
# for i in range(1000,9999):
#     c1 = i / 1000
#     c2 = (i % 1000)/100
#     c3 = (i % 100)/10
#     c4 = i % 10
#     c = c1 + c2 + c3 +c4
#     if c == a :
#        print i
#
# z = int(raw_input("Enter number:"))
# f1 = 1
# f2 = 2
# print f1
# print f2
# for i in range(3,z+1):
#     print (f1+f2 )
#     b=f1
#     f1=f2
#     f2=f1+b

# a = int(raw_input("Enter number:"))
# x=a
# while(x!=0):
#     m=x%10
#     z=m**3
#     z+=z
#     x=x/10
# print z

import math

# e = 1E-5
# a = 0.05
# b = 0.9
# h = 0.05
#
# template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
# print "-"*65
#
# x = a
# while x < b:
#     k = 1
#     s = k*(k+1)*x**k
#     S = s
#     while s > e:
#         k += 1
#         s = k*(k+1)*x**k
#         S += s
#     y = 2*x/((1-x)**3)
#     p = math.fabs(((S-y)/y))*100
#     print template.format(x, S, y, p)
#     x += h
# print "-"*65

e = 1E-5
a = 0.05
b = 0.9
h = 0.05
# template = "| {} | {} | {} | {} |"
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 0
    s = (x**(k+2)/(math.factorial(k)*(k+2)))
    S = s
    while s > e:
        k += 1
        s = (x**(k+2)/(math.factorial(k)*(k+2)))
        S += s
    y = ((x-1)*math.exp(x))+1
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65