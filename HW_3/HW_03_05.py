"""Let k- integer from 1 to 365. Assign all the variable value n
(Monday, Tuesday, ..., Saturday or Sunday), depending on which
day of the week accounted for the k-th day is not a leap year in which January 1 -
Monday."""
k = str(raw_input(range(1,365)))
n1 = "Monday", "Tuesday", "Wednesday", "Thuersday", "Friday", "Saturday", "Sunday"
n = k % 7
if n in range(1,7):
	print range(n1[0,6])