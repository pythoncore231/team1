a=int(raw_input("Number: "))
if a == 1 or a == 2:
    print "This is prime number"
else:
    p = [i for i in range(3, a/2+1) if (a % i) == 0]
    if p:
        print "This is not prime number"
    else:
        print "This is prime number"

a=int(raw_input("Enter number:"))
for i in range(1000,9999):
    c1 = i / 1000
    c2 = (i % 1000)/100
    c3 = (i % 100)/10
    c4 = i % 10
    c = c1 + c2 + c3 +c4
    if c == a :
       print i

z = int(raw_input("Enter number:"))
f1 = 1
f2 = 2
print f1
print f2
for i in range(3,z+1):
    print (f1+f2 )
    b=f1
    f1=f2
    f2=f1+b

number = int(raw_input("Please enter number: "))
str1 = str(number)
Sum = 0
Sum = sum( int(str1[i])**3 for i in range(len(str1)) )
print "Sum of the cubes: ", Sum

str1 = "tast test testas teest tust task teeth time "
sub_str = "ta"
list_str = str1.split()
list1 = [list_str[i]  for i in range(len(list_str)) if list_str[i].startswith(sub_str)]
print list1
import math

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
    s = k*(k+1)*x**k
    S = s
    while s > e:
        k += 1
        s = k*(k+1)*x**k
        S += s
    y = 2*x/((1-x)**3)
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65

e = 1E-5
a = 0.05
b = 0.9
h = 0.05
# template = "| {} | {} | {} | {} |"
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