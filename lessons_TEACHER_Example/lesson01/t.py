class A(object):
	def __init__(self, a=1, b=1):
		self.a = a
		self.b = b 
	def __eq__(self):
		return "a:{} b:{}".format(self.a, self.b)
a = A()
print a.__dict__
a.f = 1
print a.__dict__
b = A()
print b.__dict__
