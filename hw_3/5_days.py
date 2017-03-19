# 5 Days

k = int(input("day = "))

if not k in range(0, 365):
    print "Incorrect!"
else:
    # 1) with tuple
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    n = days[(k % 7)-1]
    print n

    # 2) without tuple
    numDay = k % 7
    if numDay == 1:
        n = 'Monday'
    elif numDay == 2:
        n = 'Tuesday'
    elif numDay == 3:
        n = 'Wednesday'
    elif numDay == 4:
        n = 'Thursday'
    elif numDay == 5:
        n = 'Friday'
    elif numDay == 6:
        n = 'Saturday'
    else:
        n = 'Sunday'
    print n