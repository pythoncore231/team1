class A(object):
    atr1 = "str"
    atr2 = [1,2,3]
    def __init__(self, _att3 ="arg", _atr4 = [11,12,13]):
        print self.__dict__

        self.atr3 = _att3
        self.atr4 = _atr4
    def __del__(self):
        # print "del"
        pass
    def __str__(self):
        return "{} {} {} {}".format(self.atr1,
                                    self.atr2,
                                    self.atr3,
                                    self.atr4)
    def __repr__(self):
        return "atr3:{}".format(self.atr3)

    def sum(self):
        return str(self.atr3) + str(self.atr4)


# print dir()
a = A()
a1 = A("hjfgdshjfvgjs", 999)
print a1
# a1.atr4.append(4)
# a1.atr2.append(44)
# a1.atr1 = 132
# print a.atr1,a.atr2,a.atr3,a.atr4
# print a1.atr1, a1.atr2, a1.atr3, a1.atr4
# print a.__dict__
# print a1.__dict__
# print a.sum()
# print a1.sum()
# print dir(a)
# print type(A)
# print type(a)
# del a
# print a.__dict__
# print
# print dir(a)
# print
# print A.__dict__
# print
# print dir(A)
t = a.__str__()
print ">>", t , "<<"
print [a, a1]
