class A(object):
    def __init__(self, x=1):
        self. _x = x
    def getx1(self): # method to obtain the value
        print "getA"
        return self. _x
    def setx1(self, value): # assign new value
        print "setA"
        self. _x = value
    def delx1(self): # delete attribute
        del self. _x
    # x = property(getx1, setx1, delx1, "property x")

# a = A(1)
# print a.__dict__
# print a.x
# a.x = 55
# print a.x
# print a.__dict__
class B(object):
    def __init__(self, x=10):
        self. _y = x
    # def getx1(self): # method to obtain the value
    #     print "getB"
    #     return self. _y
    def setx1(self, value): # assign new value
        print "setB"
        self. _y = value
    def delx1(self): # delete attribute
        del self. _y
    # y = property(getx1, setx1, delx1, "property x")

class C(A):
    def setx1(self, x):
        self._x = x**2
    def super_setx(self, x):
        super(C, self).setx1(x)

    # def __init__(self, x, y):
    #     super(C, self).__init__(x)

    #     super(C, self).__init__(y)
        
        

a = A(1)
b = B(1)
print a.__dict__
print b.__dict__
c = C()
print "c", c.__dict__
c.setx1(10)
print c.getx1()
c.super_setx(10)
print c.getx1()
c.setx1(10)
print c.getx1()
c.__class__ = A
c.setx1(10)
print c.getx1()
print dir(c)

b = True 
while (b):
    try:
        a = int(raw_input("a"))
        b = int(raw_input("b"))
        c = a/b
    except BaseException as error:
        # print "Error!!! ", error
        # print b
        pass
    else:
        print c
        b = False

# except exception_groupN as variableN:
#     except_caseN
# else:
#     else_case  # all's ok
# finally:
#     finally_case  # always executed
