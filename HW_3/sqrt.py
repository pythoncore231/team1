from math import sqrt

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

des = b ** 2 - 4 * a * c
print(des)

if des == 0:
    print("x = ", (b / (2 * a)))
elif des > 0:
    print("x1 =", (str(b + sqrt(des) / 2 * a)), "x2 =", (str(b - sqrt(des) / 2 * a)))
else:
    print("false")