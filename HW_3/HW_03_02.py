"""2) Enter three values (year, month, day) in the relevant variables. Identify
whether your entries correspond to the correct record date."""



Year = int(raw_input("Year = "))
Month = int(raw_input("Month = "))
Day = int(raw_input("Day = "))
if Year >= 2017:
	print  "{}/{}/{}".format(Year,Month,Day)
elif Year < 2017:
	print "{}/{}/{} it is past tense!".format(Year,Month,Day)
elif Month == 1 or in range(3.12):
	print "{}/{}/{}".format(Year,Month,Day)
elif Day in range(1,31) and  Month not 2:
	print "{}/{}/{}".format(Year,Month,Day)
elif Day in range(1,29) and Month == 2 and Year % 4 == 0:
	print "{}/{}/{}".format(Year,Month,Day)
elif Day in range(1,28) ande Month == 2 and Year % 4 > 0:
	print "{}/{}/{}".format(Year,Month,Day)
else:
	print "You inser incorrect date"