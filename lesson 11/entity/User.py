# -*- coding: utf-8 -*-
from base import Base


class User(Base):
    def __init__(self, id=0, first_name=None, last_name=None, age=None):
        super(User, self).__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "id:{} first_name:{} last_name:{} age:{}".format(self.id, self.first_name, self.last_name, self.age)

    def __repr__(self):
        return "{}".format(self.first_name)

    def to_unicode(self):
        return unicode("{} {} {} {}".format(self.id, self.first_name, self.last_name, self.age))
