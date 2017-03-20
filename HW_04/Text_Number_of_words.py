'''
Created on Mar 20, 2017

@author: vodachuk
'''
from Count_of_words import string
s = raw_input("Enter some symbols: ")
i = 0
for n in string.split():
    if n.find(s) == 0 :
        print n
        i += 1
print "Count of words: ", i
