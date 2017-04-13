from base import Base


class Group(Base):
    def __init__(self, name=None, members=None):
        super(Group, self).__init__(id)
        self.name = name
        self.members = members

    def __str__(self):
        temp = "name: {} members:".format(self.name)
        for member in self.members:
            temp += "\n\t\t{}".format(member)
        return temp

    def __repr__(self):
        return "{}".format(self.name)

    def to_unicode(self):
        temp = unicode("{} ".format(self.name))
        for member in self.members:
            temp += "{},".format(member.id)
        return temp