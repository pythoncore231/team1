str1 = "test"
print str1, type(str1)
print dir(str1)

str2 = "age: %s , my name %s" % ( 19, "Anna")
str3 = "my name {0} {1} {0} {1}, age: {1}".format("Anna", 19)
# print str2
# print str3
# print len(str3)
str4 = "I'm programisT"
# print str4, str4[1]
# print str4[0:5], str4[:5],  str4[5:]
# print str4[::3]
# print str4[::-1], str4[-1], str4[-5:len(str4)-1]
str5 = str4 + str3
# print str5
str6 = u"test"
print str6, type(str6)


