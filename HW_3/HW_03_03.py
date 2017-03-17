#3 Math 
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
