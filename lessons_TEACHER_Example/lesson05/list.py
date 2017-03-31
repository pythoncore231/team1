l = list()
print l, type(l)
l = []
print l, type(l)
l = [1, "2", 1.3]
print l, type(l)
for i in l:
    print i, type(i)
print dir(l)
l.append(10)
l.append( [1,2,3,4,5] )
l.extend( [1,2,3,4,5] )
l.append( "str" )
l.extend( "str" )
print l
print l.count(1)
print l.index(1,2,len(l))
l.insert(1, "test")
print l
l[1] =  "!!!!"
print l
a = l.pop()
print a
print l
a = l.pop(1)
print a
print l
try:
    l.remove(1111)
except:
    print "Error!!!!"
print l
l.reverse()
print l
print l[::-1]
l.sort()
print l
l.sort(reverse=True)
print l
print help(l.sort)
print len(l), l.__len__()
n=10
print [i**2 for i in range(n)]
l = []
print l
l.append("sadf")
print l
l = [1]
print l, type(l)





