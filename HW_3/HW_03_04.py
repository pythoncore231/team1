#4 Given three arbitrary numbers. Determine whether you can build triangle with sides of lengths; If so, then print it perimeter and area.
from math import sqrt

a = int(raw_input("A = "))
b = int(raw_input("B = "))
c = int(raw_input("C = "))
p = (a + b + c)
s = str(sqrt(p*(p - a)*(p - b)* (p - c)))
R1 = (a < (b + c))
R2 = (b < (a + c))
R3 = (c < (a + b))
if R1 and R2 and R3 == True:
	print "P(ABC) = {}, S(ABC) = {}".format(p, s)