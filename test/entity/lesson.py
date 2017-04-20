from base import Base

class Lesson(Base):
    def __init__(self, name, teacher):
        super(Lesson, self).__init__()
        self.name = name
        self.teacher = teacher
    def __repr__(self):
        return '{} {}'.format(self.name, self.teacher)
    def __str__(self):
        return 'name: {} teacher: {}'.format(self.name, self.teacher)
    def to_unicode(self):
        return unicode('{} {}'.format(self.name, self.teacher))