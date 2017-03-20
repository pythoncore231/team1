year = int(raw_input('Year : '))
if year % 4 == 0 : print ("It's a leap year!")
else : print ("This is not a leap year!")

# a = int(raw_input('A : '))
# b = int(raw_input('B : '))
# c = int(raw_input('C : '))
# d=b*b-4*a*c
# if d<0 : print ("Nemaye koreniv")
# elif d > 0 :
#                     x1 = (-b-(d**0.5))/(2*a)
#                     x2 =(-b+(d**0.5))/(2*a)
#                 print x1
#                 print()
#     else : x3 = (-b/(2*a))
# print x3

a = int(raw_input('A : '))
b = int(raw_input('B : '))
c = int(raw_input('C : '))

if (a+b<c) or (a+c<b) or (b+c<a) :
                print ("Trykutnik nemozluvo utvoryty")
else : p = (a+b+c)/2; s = (p*(p-a)*(p-b)*(p-c))**0.5; P=a+b+c; print ("S= {},\nP={}".format(s, P) )