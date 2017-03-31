str1 = "test"
print str1, type(str1)
str2 = u"test"
print str2, type(str2)
print str1[0], str1[1], str1[-2], str1[-1]
print str1[0] == str1[-4]
print str1[0:3], str1[:3], str1[2:], str1[-3:4]
print str1[::2], str1[::-2]
# print dir(str1)
# print help(str)
print "t:", str1.count("t"), "e:", str1.count("e"), "stt:", str1.count("stt"), 
str3 = "    test test            "
print 
print "|", str3, "|"
print "|", str3.strip(), "|"
print str3.find("t", 0,4)
print "t:%d e:%d s:%s" % (str1.count("t"), str1.count("e"), str1.count("s"))
print "e:{1} t:{0} s:{2}".format(str1.count("t"), str1.count("e"), str1.count("s"))

