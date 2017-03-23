#Given a number N, to bring the first N Fibonacci numbers.

Number = int(raw_input("Enter the start number here "))
Number1 = int(raw_input("Enter the end number here "))

Fibonacci = n
for n in Fibonacci:
    if n < 2:
        print n
    print Fibonacci(n-2) + Fibonacci(n-1)

print map(Fibonacci, range(Number, Number1))