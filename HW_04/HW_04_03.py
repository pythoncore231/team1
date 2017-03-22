#Given a number N, to bring the first N Fibonacci numbers.

Number = int(raw_input("Enter the start number here "))
Number1 = int(raw_input("Enter the end number here "))

fib = n
for n in fib:
    if n < 2:
        print n
    print fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))