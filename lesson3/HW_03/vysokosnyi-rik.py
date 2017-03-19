from math import *

k = input ("Vvedy rik k = ")

if k%4 == 0:
    if k%100 != 0 or (k%100 == 0 and k%400 == 0):
        print "Vysokosnyi rik"
    else: print  "Ne vysokosnyi rik"
else: print  "Ne vysokosnyi rik"
