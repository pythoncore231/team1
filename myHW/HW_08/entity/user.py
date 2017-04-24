from base import Base

class User(Base):
    def __init__(self, fistname = None, lastname = None, age = None):
        super(User, self).__init__()
        self.firstname = fistname
        self.lastname = lastname
        self.age = age
    def __str__(self):
        return "Firstname:{} Lastname:{} Age:{}".format(self.firstname, self.lastname, self.age)
    def __repr__(self):
        return "{}".format(self.firstname)
    def to_unicode(self):
        return unicode("{} {} {}".format(self.firstname, self.lastname, self.age))
