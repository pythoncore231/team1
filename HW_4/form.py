import math

# a
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65
x = a
while x < b:
    k = 1
    s = k * (k + 1) * x ** k
    S = s
    while s > e:
        k += 1
        s = k * (k + 1) * x ** k
        S += s
    y = 2 * x / ((1 - x) ** 3)
    p = math.fabs(((S - y) / y)) * 100
    print template.format(x, S, y, p)
    x += h
print "-"*65

# b
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 0
    s = (x**(k+2)/(math.factorial(k)*(k+2)))
    S = s
    while s > e:
        k += 1
        s = (x**(k+2)/(math.factorial(k)*(k+2)))
        S += s
    y = ((x-1)*math.exp(x))+1
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65


# c
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 1
    s = k * (k + 2) * (x ** k)
    S = s
    while s > e:
        k += 1
        s = k * (k + 2) * (x ** k)
        S += s
    y = (x * (3 - x)) / ((1 - x) ** 3)
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65

# d
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 1
    s = ((-1)**k) * (x ** k) * ((5 + 2 * (k-1)) / 2 * k)
    S = s
    while s > e:
        k += 1
        s = ((-1) ** k) * (x ** k) * ((5 + 2 * (k - 1)) / 2 * k)
        S += s
    y = (1. + x) ** ( - 5. / 2)
    p = math.fabs(((S - y) / y)) * 100
    print template.format(x, S, y, p)
    x += h
print "-" * 65

# e
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 1
    s = x ** ( k-1 ) * (1 + 2 * (k - 1))
    S = s
    while s > e:
        k += 1
        s = x ** (k - 1) * (1 + 2 * (k - 1))
        S += s
    y = ((1 + x) / ((1 - x)**2))
    p = math.fabs(((S - y) / y)) * 100
    print template.format(x, S, y, p)
    x += h
print "-" * 65
