n = int(raw_input("number = "))
f, s = 1, 1
print f, s,
for i in range(n - 2):
    f, s = s, s + f
    print s,