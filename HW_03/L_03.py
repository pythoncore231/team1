a=1
b=5
x=1
if a<x<b:
    print True
else:
    print False

# result = True if x>a and x<b else False

str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut"
l=len(str1)
if l > 100:
    print "Too long string"
else:
    print "a:{} e:{} i:{} o:{} u:{}".format(str1.count("a"), str1.count("e"), str1.count("i"), str1.count("o"), str1.count("u"))