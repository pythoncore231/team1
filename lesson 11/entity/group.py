# -*- coding: utf-8 -*-
from base import Base


class Group(Base):
    def __init__(self, id=0, name=None, members=None):
        super(Group, self).__init__(id)
        self.name = name
        self.members = members

    def __str__(self):
        return "id:{} name:{} members:{}".format(self.id, self.name, self.members)

    def __repr__(self):
        return "{}".format(self.name)

    def to_unicode(self):
        return unicode("{} {} {}".format(self.id, self.name, [user.to_unicode() for user in self.members]))
