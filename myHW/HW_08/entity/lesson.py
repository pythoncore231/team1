from base import Base

class Lesson(Base):
    def __init__(self, name = None, teacher = None):
        super (Lesson, self).__init__()
        self.name = name
        self.teacher = teacher
    def __str__(self):
        return "Subject: {} Teacher: {}".format(self.name, self.teacher)
    def __repr__(self):
        return "{}".format(self.name)
    def to_unicode(self):
        return unicode("{} {}".format(self.name, self.teacher))
