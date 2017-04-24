from base import Base
class Group(Base):
    def __init__(self, id=0, name=None, members=None):
        super(Group,self).__init__(id)
        self.name = name
        self.members = members
    def __str__(self):
        return "id:{} name:{} member:{}".format(self.id, self.name, self.members)
    def __repr__(self):
        return "member: {}".format(self.members)
    def to_unicode(self):
        return unicode("{} {} {}".format(self.id, self.name, self.members))

