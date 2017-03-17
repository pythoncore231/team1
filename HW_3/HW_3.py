#1
a = int(raw_input())
if a == 365:
	print "It is a leap year!"
elif a == 366:
	print "This is not a leap year"

#2
Year = int(raw_input())
Month = int(raw_input())
Day = int(raw_input())
if Year >= 2017:
	print "It is {}".format(Year)
elif Month in range(1,12):
	print "It is {}".format(Month)
elif Day in range(1,31):
	print "it is {}".format(Day)
print Year, Month, Day

#3
a = 15
b = 40
c = 15
D = b ** 2 - 4*a*c
if D < 0:
	print "There is no answer"
elif D == 0:
	print "There is one answer {}".format(b / 2*c)
elif D > 0:
	print "There are two answers x1 = {}, x2 = {}".format((b+D**0.5)/(2*a),
				(b-D**0.5)/(2*a))

#4
a = 15
b = 12
c = 15
if a + b + c >= 3:
	print "We are able to create the triangular"
