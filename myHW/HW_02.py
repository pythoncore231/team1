string = """
The Zen of Python, by Tim Peters

Beautiful is better
than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

a1 = string
print " better: {} never : {} is : {}".format(a1.count("better"), a1.count("never"), a1.count("is"))
a2 = string
print a2.upper()

a3 = string
print a3.replace("i", "&")

z = 4758
a = z / 1000
b = (z % 1000) / 100
c = (z % 100) / 10
d = z % 10
print a, b, c, d
print a * b * c * d

a = 3
b = 5
# # print "Number a: {0} Number b: {1}".format( a.'a', 'b')
#
print a
print b

a = b + a
b = a + b
a = b - a
b = b - 2 * a

print a
print b

import math

x = float(raw_input("X:"))
y = float(raw_input("Y:"))

a = (math.sqrt(math.fabs(x-1))-pow(math.fabs(y),0.3))/(1+((x**2)/2)+(y**2)/4)

print a

x = float(raw_input("X:"))
z = float(raw_input("Z:"))

b = x*(math.atan(z)+math.exp(-(x+3)))

print b

x = float(raw_input("X:"))
y = float(raw_input("Y:"))
z = float(raw_input("Z:"))

a = (3 + math.exp(y-1))/(1 + (x**2)*math.fabs(y-math.tan(z)))

print a

x = float(raw_input("X:"))
y = float(raw_input("Y:"))

b = 1 + math.fabs(y - x) + (((y - x)**2)/2) + ((math.fabs((y - x)**2))/3)

print b

x = float(raw_input("X:"))
y = float(raw_input("Y:"))

a = (1 + y)*(((x+y)/x**2+4)/((math.exp(-x-2)+1)/(x**2+4)))

print a

x = float(raw_input("X:"))
y = float(raw_input("Y:"))
z = float(raw_input("Z:"))

ds = 1 - math.cos(2*z)
b = (1+math.cos(y-2))/x**4/(2 + ds)

print b


x = float(raw_input("X:"))
y = float(raw_input("Y:"))

a = y + (x / ((y**2) + math.fabs(x**2) / y + (x**3) / 3))

print a

z = float(raw_input("Z:"))

b = 1 + math.pow(math.tan(z/2),2)

print b

x = float(raw_input("X:"))
y = float(raw_input("Y:"))

a = (2*math.cos(x - math.pi/6))/(1/(2+math.pow(math.sin(y),2)))

print a

z = float(raw_input("Z:"))

b = 1 + (z**2/(3 + z ** 2 / 5))

print b

x = float(raw_input("X:"))
y = float(raw_input("Y:"))

a = (1 + math.pow(math.sin(x+y),2))/(2 + math.fabs((x - 2*x)/1+(x**2)*(y**2)))

print a

z = float(raw_input("Z:"))

b = math.pow(math.cos(math.atan(1/z)),2)

print b

x = float(raw_input("X:"))
y = float(raw_input("Y:"))
z = float(raw_input("Z:"))

a = math.log(math.fabs((y-math.sqrt(math.fabs(x)))*(x - (y/((z + x**2) / 4)))))

print a

x = float(raw_input("X:"))

a = x - (x**2/math.factorial(3)) + (x**5/math.factorial(5))

print a
