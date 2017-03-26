#Put the numbers to check whether a given number is a integer

n = input(" it must be integer : ")
while n:
    if n % 2 != 0 or n % 3 != 0:
    	print "it\'s an integer"
    elif n == 2 and n == 3:
    	print "it\'s an integer"
    else:
    	print "it\'s not integer"
    break



