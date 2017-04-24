k = input("Enter k in range 1 to 365")
day = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

n = k % 7

if n == 1:
    print day[0]
elif n == 2:
    print day[1]
elif n == 3:
    print day[2]
elif n == 4:
    print day[3]
elif n == 5:
    print day[4]
elif n == 6:
    print day[5]
elif n == 7:
    print day[6]