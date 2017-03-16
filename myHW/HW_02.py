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
# print "Number a: {0} Number b: {1}".format( a.'a', 'b')

print a
print b

a = b + a
b = a + b
a = b - a
b = b - 2 * a

print a
print b
