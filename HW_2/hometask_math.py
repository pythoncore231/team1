string = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
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

if len(string) > 100:
    print("String is long")
else:
    print(string.count("a"))
    print(string.count("e"))
    print(string.count("i"))
    print(string.count("o"))

from math import sqrt

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

des = b ** 2 - 4 * a * c
print(des)

if des == 0:
    print("x = ", (b / (2 * a)))
elif des > 0:
    print("x1 =", (str(b + sqrt(des) / 2 * a)), "x2 =", (str(b - sqrt(des) / 2 * a)))
else:
    print("false")










