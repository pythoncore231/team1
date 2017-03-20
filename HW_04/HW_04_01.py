#Find all Four digit numbers, which tsyfer amount equal to a given number
from math import fsum
number = "20"
for i in number:
	if i + i + i + i == number:
		if i > 1000 and i < 9999:
			print str(i + i + i + i)