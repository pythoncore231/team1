"""Let k- integer from 1 to 365. Assign all the variable value n
(Monday, Tuesday, ..., Saturday or Sunday), depending on which
day of the week accounted for the k-th day is not a leap year in which January 1 -
Monday."""
k = int(raw_input("day = : "))
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

