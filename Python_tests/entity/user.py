'''
Created on Apr 13, 2017

@author: vodachuk
'''
"""
    First name (string)
    Last name (string)
    Age (int)
"""
from base import Base

class User(Base):
    def __init__(self, id = 0, FirstName = None, LastName = None, age = None):
        super(User, self).__init__(id)
        self.id = id
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = age
        
    def __str__(self):
        return "id: {} FirstName: {} LastName: {} age: {}".format(self.id, self.FirstName, self.LastName, self.age)
    def __repr__(self):
        return "id: {} FisrtName: {} LastName: {} age: {}".format(self.id, self.FirstName, self.LastName, self.age)
        
    def to_unicode(self):
        return unicode("{} {} {} {}".format(self.id, self.FirstName, self.LastName, self.age))
        