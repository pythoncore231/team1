# 1
str1 = "Hello world!"
print "a:{}".format(str1.count("a"))
print "e:{}".format(str1.count("e"))
print "i:{}".format(str1.count("i"))
print "o:{}".format(str1.count("o"))
print "u:{}".format(str1.count("u"))
print "y:{}".format(str1.count("y"))

# 2
a = 1234.5678
dot = str(a).find(".")
str2 = str(a)[dot-3:dot] + str(a)[dot+1:dot+4]
print int(str2[0]) + int(str2[1]) + int(str2[2]) + int(str2[3]) + int(str2[4]) + int(str2[5])
