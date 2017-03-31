t = tuple()
t = (1,)
t = ("a",1)

print t, type(t)
print dir(t)
for i in (i**2 for i in range(10)):
    print i,
print 
print len(t), t.__len__()
a = 1
b = 2
c = 3
c, a, b  = b, a, c
print a, b, c
l = [i**2 for i in range(999)]
t = tuple(l)
print l.__sizeof__()
print t.__sizeof__()

