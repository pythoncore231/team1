str = "  wer 444, tyYUp ddf  "
print "a:", str.count("a"), ",", "e:", str.count("e"), ",", "i:", str.count("i"), ",", "o:", str.count("o"), ",", "u:", str.count("u")
print "a:{} e:{} i:{} o:{} u:{}".format(str.count("a"), str.count("e"), str.count("i"), str.count("o"), str.count("u"))
print "e:{1} a:{0} o:{3} u:{4} i:{2}".format(str.count("a"), str.count("e"), str.count("i"), str.count("o"), str.count("u"))

points = 19.5
total = 22
print ('Correct answers: {:.2%}'.format(points/total))

d = 24544.784245
num = "%f" % d
pos = num.find(".")

print(int(num[pos-3]) + int(num[pos-2]) + int(num[pos-1]) + int(num[pos+1]) + int(num[pos+2]) + int(num[pos+3]))

d = "2546.1379"
a = d.index(".")
print a
print (int(d[a-3])+int(d[a-2])+int(d[a-1])+int(d[a+1])+int(d[a+2])+int(d[a+3]))