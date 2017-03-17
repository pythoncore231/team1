# -*- coding: utf-8 -*-

year = float(raw_input('Input year: '))

if year % 4 == 0 and year % 100 != 0:
    print "It's a leap year!"
elif year % 400 == 0:
    print "It's a leap year!"
else:
    print "This is not a leap year!"
