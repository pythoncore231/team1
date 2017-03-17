#1Enter a value (year), display a message "It's a leap year!" if the year

year = int(raw_input("Year = "))
if year == 366 or year % 4 == 0:
	print "It is a leap year!"
elif year == 365 or year % 4 > 0:
	print "This is not a leap year"


