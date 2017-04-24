class TTT(object):
    def __init__(self, x, y, z):
        self.x = x
        self._y = y 
        self.__z = z
    def __str__(self):
        return "{} {} {}".format(self.x,
                                 self._y,
                                 self.__z)
    def set_z(self, new_z):
        self.__z = new_z
    def __t_z__(self, new_z):
        self.__z = new_z
p = TTT(1,2,3)
p1 = TTT(1,2,3)
print p
p.x = 10
p._y = 20
p.__z = 30
p.set_z(99)
print p.__dict__
print p
print p1.__dict__
# print p1.__t_z(99999)
print TTT.__dict__
# print p
# print p._T__z

        