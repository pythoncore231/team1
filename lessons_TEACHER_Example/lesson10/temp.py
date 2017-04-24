class T(object):
    cl = 1
    def __init__(self, arg=None):
        self.arg = arg
    def __str__(self):
        return str(self.arg)
    def __repr__(self):  
        return str(self.arg)
    def __hash__(self):
        return self.arg
    def __eq__(self, other):
        return self.arg > self.arg

    @staticmethod
    def foo():
        return "foo"

    def boo(self):
        print type(self)
        print "self: ", self.__dict__
        # def temp(_self):
        #     return _self.__dict__
        # self.get_str = temp
        return "boo " + str(self.arg)

    @classmethod
    def cl_m(cls):
        print type(cls)
        print "cls: ", cls.__dict__
        def temp(self):
            return self.__dict__
        cls.get_str = temp
        return "cl_m"

# d = {}
# d["test"] = 1
# t = T(3)
# print t
# d[t] = 2
# t = T(1)
# print t
# d[t] = 3
# print d
t = T(1)
t1 = T(5)
# print t.foo()
# print T.foo()
print t.boo()
print T.cl_m()
# print t.__dict__
# print t1.__dict__
# print t.get_str()
# print t1.get_str()


# @classmethod
# def temp_coo(cls):
#     return "foo"
# T.coo = temp_coo