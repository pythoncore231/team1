from math import *

year = int(input("Year = "))
month = int(input("month = "))
day = int(input("day = "))

if 1 <= day <= 31 and (month%2)!=0 and  1 <= month <=12:
    print("right")
    print("{}.{}.{}".format(year, month, day))
elif 1 <= day <= 28 and month == 2:
    print("right")
    print("{}.{}.{}".format(year, month, day))
elif day % 4 == 0 and day % 100 != 0 or day % 400 == 0 and 1 <= day <= 29 and day == 2:
    print("right")
    print("leap year")
    print("{}.{}.{}".format(year, month, day))
else:
    print("false")