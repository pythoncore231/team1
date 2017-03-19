# 2 Date is correct/incorrect

year = int(raw_input("year = "))
month = int(raw_input("month = "))
day = int(raw_input("day = "))

if 0 < len(str(year)) <= 4:
    print "Year is correct"
else:
    print "Year is incorrect"

if 0 < month <= 12:
    print "Month is correct"
else:
    print "Month is incorrect"

leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
if day > 0 and (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
                                month in (4, 6, 9, 11) and day <= 30 or \
                                leapYear and month == 2 and day <= 29 or \
                                not leapYear and month == 2 and day <= 28):
    print "Day is correct"
else:
    print "Day is incorrect"