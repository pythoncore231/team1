#-*- coding: utf-8 -*-
import math
#Quadratic equation
a = float(input('Input a='))
b = float(input('Input b='))
c = float(input('Input c='))
d= (b**2)-(4*a*c)
print 'D=', d
if d < 0:
    print "No results"
elif d==0:
    x=-b/(2.0*a)
    print 'x=', x
else:
    x1=(-b+(d**0.5))/(2*a)
    x2=(-b-(d**0.5))/(2*a)
    print 'x1=', x1
    print 'x2=', x2

#Triangle
a = float(input('Input 1st side='))
b = float(input('Input 2nd side='))
c = float(input('Input 3rd side='))
p=a+b+c
p2=p/2
if a<(b+c) and b<(a+c) and c<(a+b):
    print 'P=', p ,'S={}'.format(str(math.sqrt(p2*(p2-a)*(p2-b)*(p2-c))))
else:
    print 'Incorrect'

#Leap Year
y=int(input('Input year:'))
if y%4==0:
    print 'Leap year!' 
else:
    print 'This is not a leap year.'

y=int(input('Input year.'))
print 'Leap year!' if y%4==0 else 'This is not a leap year.'


#Check correct date
y=int(input('Input year:'))
m=int(input('Input number of month:'))
if 1<= m <= 12:
    d=int(input('Input number of day:'))
    if 1<=d<=28 and m==2 or d==29 and m==2 and y%4==0:
        print 'Year: {}, Month: {}, Day: {}'.format(y, m, d)
    elif 1<=d<=30 and m in (4, 6, 9, 11)  or  1<=d<=31 and m!=2:
        print 'Year: {}, Month: {}, Day: {}'.format(y, m, d)
    else:
        print 'Incorrect format of date'
else:
    print 'Incorrect format of date'

#Day of year
d=int(input('Input number of day: '))
l=d%7
if d>365:
    print 'Incorrect number of day'
elif l==1:
    print 'Monday'
elif l==2:
    print 'Tuesday'
elif l==3:
    print 'Wednesday'
elif l==4:
    print 'Thursday'
elif l==5:
    print 'Friday'
elif l==6:
    print 'Satursday'
else:
    print 'Sunday'