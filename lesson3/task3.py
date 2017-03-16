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


#print string

#print "count of better", string.count("better")
#print "count of never", string.count("never")
#print "count of is", string.count("is")

count_of_str = string.count("")

if count_of_str > 1000090:
    print count_of_str
else: 
    print string.count("a")+string.count("e")+string.count("o")

from math import *

a = input ("a = ")
b = input ("b = ")
c = input ("c = ")

D = b**2 - 4*a*c

print D

if D < 0:
    print "Nema"
elif D == 0:
     print "Odyn"
else:
    print "dva"






