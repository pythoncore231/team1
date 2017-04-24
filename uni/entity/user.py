from base import Base

class User(Base):
    def __init__(self, id=0, firstname=None, lastname=None, age=None ):
        super(User,self).__init__(id)
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return "id:{} firstname:{} lastname:{} age:{} ".format(self.id, self.firstname, self.lastname, self.age)
    def __repr__(self):
        return "{}".format(self.firstname)
    def to_unicode(self):
        return unicode("{} {} {}".format(self.id, self.firstname, self.lastname, self.age))