from base import Base

class User(Base):
    def __init__(self, firstname=None, lastname=None, age=0):
        super(User, self).__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.age)
    def __str__(self):
        return 'firstname: {}, lastname: {}, age: {}'.format(self.firstname, self.lastname, self.age)
    # def __int__(self):
    #     return ({}.format(self.age))
    def to_unicode(self):
        return unicode('{} {} {}'.format(self.firstname, self.lastname, self.age))