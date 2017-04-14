'''
Created on Apr 13, 2017

@author: vodachuk
'''
"""
    Name (string)
    Members (list(user))
"""

from base import Base

class Group(Base):
    def __init__(self, id = 0,  name = None, member = None):
        super(Group, self).__init__(id)
        self.id = id
        self.name = name
        self.member = member
        
        
    def __str__(self):
        return "id: {} name: {} member: {}".format(self.id, self.name, self.member)
    def __repr__(self):
        return "id: {} name: {} member: {}".format(self.id, self.name, self.member)
        
    def to_unicode(self):
        return unicode("{} {} {}".format(self.id, self.name, self.member))