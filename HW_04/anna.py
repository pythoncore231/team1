from math import *

def doublefact(x):
    if x > 0:
        return doublefact(x - 2) * x
    else:
        return 1

e = 1E-5  # 10**-5
a = 0.05
b = 0.9
h = 0.1
fS = ('k*(k+1)*x**k', '(1./(factorial(k)*(k+2)))*x**(k+2)', 'k*(k+2)*x**k', \
      'doublefact(2*k+3)/doublefact(2*k)*(-x)**k', '(2*k+1)*x**k')
fy = ('2*x/((1-x)**3)', '(x-1)*e**x+1', 'x*(3-x)/(1-x)**3', '(1+x)**(5./2)', '(1+x)/(1-x)**2')
tk = (1, 0, 1, 0, 0)
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
for i in range(len(fS)):
    print "{}) {}".format(i + 1, fS[i])
    print "-" * 65
    print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
    print "-" * 65
    x = a
    while x < b:
        k = tk[i]
        s = eval(fS[i])
        S = s
        while s > e:
            s = eval(fS[i])
            S += s
            k += 1
            y = eval(fy[i])
        p = fabs(((S - y) / y)) * 100
        print template.format(x, S, y, p)
        x += h
    print "-" * 65