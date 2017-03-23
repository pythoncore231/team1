# a=int(raw_input("Number: "))
# if a>1:
#     for i in range(2,a):
#         if (a%i)==0:
#             print(a,i,"It's not a prime number")
#             continue
#         else: print (a,i,"It's a prime number")
# else: print (a,"It's not a prime number")

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

# a = int(raw_input("Enter number:"))
# x=a
# while(x!=0):
#     m=x%10
#     z=m**3
#     z+=z
#     x=x/10
# print z