# # a=1
# # b=5
# # x=1
# # if a<x<b:
# #     print True
# # else:
# #     print False

# # # result = True if x>a and x<b else False

# str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut"
# l=len(str1)
# if l > 100:
#     print "Too long string"
# else:
#     print "a:{} e:{} i:{} o:{} u:{}".format(str1.count("a"), str1.count("e"), str1.count("i"), str1.count("o"), str1.count("u"))
a = float(input('Input a='))
b = float(input('Input b='))
c = float(input('Input c='))
d= (b**2)-(4*a*c)
print 'D=', d
if d < 0:
    print "No results"
elif d==0:
    x=-b/(2.0*a)
    print 'x=', x
else:
    x1=(-b+(d**0.5))/(2*a)
    x2=(-b-(d**0.5))/(2*a)
    print 'x1=', x1
    print 'x2=', x2