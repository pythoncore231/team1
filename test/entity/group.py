from base import Base

class Group(Base):
    def __init__(self, name, students):
        super(Group, self).__init__(id)
        self.name = name
        self.students = students

    def __repr_(self):
        return 'Group {}, {} students'.format(self.name, len(self.students))

    def __str__(self):
        return 'Group {} {} students'.format(self.name, len(self.students))

    def to_unicode(self):
        _group = unicode('Group {}\n'.format(self.name))
        for student in self.students:
            _group += '{} {}\n'.format(student.id)
        return _group
