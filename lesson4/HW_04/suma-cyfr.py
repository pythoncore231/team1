n = raw_input("Vvedy chyslo ")
n = int(n)
sm = 0
for i in range(9,20):
    s= str(i)
    print "S= ", s
    for j in s:
        j1 = int(j)
        print "J1= ", j1
        sm += j1
        print "sm= ", sm
    if sm == n:
        print i
#
#
#    k = int(i)
#    s += k**3
#print s