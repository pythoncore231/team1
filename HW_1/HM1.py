"""my 
first 
hometask"""
numbers = range(1,11)
print numbers[3::]
print numbers[:3:]
print numbers[::3]
print numbers[::-1]
"""little
practise"""

def math(x):
	#create function math
	return x * 3 
	#it return number * 3
def math1(x):
	if x % 3 == 0:
		#it one more function that call first function
		return str(math(x)) + " ZERO"
	elif x - 12 < 0:
		return str(math(x)) + " less then 0"
	elif x > 0:
		return str(math(x)) + " bigger then zero"
print math(3) * 3
print math1(3)

