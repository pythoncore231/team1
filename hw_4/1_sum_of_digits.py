num = int(raw_input("num = "))
count = int(raw_input("count of digits = "))

for i in range(10 ** (count - 1), 10 ** count):
    strnum = str(i)
    sum = 0
    for j in range(len(strnum)):
        sum += int(strnum[j])
    if sum == num:
        print i