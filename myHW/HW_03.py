import math

year = raw_input("Please enter year: ")
month = int(raw_input("Please enter month: "))
day = int(raw_input("Please enter day: "))

if len(str(year)) and (0 < month <= 12) and (0 < day <= 31):
    print ("This is a proper date format")
else:
    print "This is not a valid date format"


a = float(raw_input("Please enter a: "))
b = float(raw_input("Please enter b: "))
c = float(raw_input("Please enter c: "))
D = (math.fabs(b**2 - 4*a*c))**0.5

if a != 0:
    x1 = (-b + D) / 2*a
    x2 = (-b - D) / 2*a
    if x1 == x2:
        print "This function has only one root: ", x1
    else:
        print "This function has two roots: ", x1, x2
else:
    x = -c/b
    print "a = 0 and x = ", x


a = int(raw_input('A : '))
b = int(raw_input('B : '))
c = int(raw_input('C : '))

if (a+b<c) or (a+c<b) or (b+c<a) :
                print ("Triangle can't be created")
else : p = (a+b+c)/2; s = (p*(p-a)*(p-b)*(p-c))**0.5; P=a+b+c; print ("S= {},\nP={}".format(s, P) )

k_day = int(raw_input("Please enter k-day of year: "))
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 1 <= k_day <= 7:
    print "k-day is ", week_days[k_day-1]
else:
    if 8 <= k_day <= 365:
        week_day = k_day - (k_day / 7) * 7
        print "k-day is", week_days[week_day-1]
    else:
        print "Wrong day"