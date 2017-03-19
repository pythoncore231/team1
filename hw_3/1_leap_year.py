# 1 Leap-year / non-leap year

year = int(raw_input("year = "))

if year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0:
    print "It's a leap year!"
else:
    print "This is not a leap year!"
