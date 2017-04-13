from base import Base

class User(Base):
    def __init__(self, id=0, name=None, capacity=None):
        super(Room,self).__init__(id)
        self.name = name
        self.capacity = capacity
    def __str__(self):
        return "id:{} name:{} capacity:{}".format(self.id, self.name, self.capacity)
    def __repr__(self):
        return "{}".format(self.name)
    def to_unicode(self):
        return unicode("{} {} {}".format(self.id, self.name, self.capacity))