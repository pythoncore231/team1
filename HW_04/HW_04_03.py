#Given a number N, to bring the first N Fibonacci numbers.

# N = input("Enter N: ")
# fib, fib1 = 0, 1
# for i in range(N):
# 	print fib, fib1 == fib1, fib + fib1
	

n = input("n : ")
a, b = 0, 1
for i in range(n):
	print a
	a, b = b, a + b
