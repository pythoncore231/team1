N = int(input("Enter Natural number: "))
n = len(str(N))
sum = 0
for i in range(n):
    g = int(str(N)[i]) ** 3
    sum += g
print sum