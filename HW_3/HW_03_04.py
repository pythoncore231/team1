year = input("Year = ")
day = input("Day = ")
month = input("Month = ")
#y = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if ((1 <= day <= 31) and not ((month % 2) == 0)):
    print "{}.{}.{}".format(day,month,year)
elif ((1 <= day <= 28) and (month  == 2)):
    print "{}.{}.{}".format(day,month,year)
elif (((year % 4)) == 0) and ((1 <= day <= 29) and (month  == 2)):
    print "{}.{}.{}".format(day,month,year)
else:
    print "Incorrect input!!!"