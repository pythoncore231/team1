
class Sheduler(object):
    def __init__(self, room=None, lesson=None, group=None, para=0):
        self.room = room
        self.lesson = lesson
        self.group = group
        self.para = para

    def __str__(self):
        return "Sheduler:\n\troom: {} \n\tlesson: {} \n\tgroup: {} \n\tpara: {}".format(self.room, self.lesson, self.group, self.para)

    def __repr__(self):
        return "{}-{}-{}".format(self.room.name, self.lesson.name, self.group.name)

    def to_unicode(self):
        return unicode("{} {} {} {}".format(self.room.name, self.lesson.name, self.group.name, self.para))