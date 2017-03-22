num = int(raw_input("num = "))
testNumbers = (2, 3, 5, 7)

for i in testNumbers:
    if not num == i and not num % i:
        result = False
        break
    else:
        result = True
print result