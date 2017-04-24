n = input("Enter the number: ")
k = 0
for i in range(1, n):
    if ( n % i ) == 0:
        k += 1
if k == 1:
    print "This is a prime number!"
else:
    print "It's not a prime number!"