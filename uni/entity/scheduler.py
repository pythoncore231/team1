from base import Base

class Scheduler(Base):
    def __init__(self,id=0,  room=None, lesson=None, group=None):
        super(Scheduler,self).__init__(id)
        self.room = room
        self.lesson = lesson
        self.group = group

    def __str__(self):
        return "para:{} room:{} lesson:{} group:{}  ".format(self.id, self.room, self.lesson, self.group)

    def __repr__(self):
        return "lesson:{}".format(self.lesson)

    def to_unicode(self):
        return unicode("{} {} {} {}".format(self.id, self.room, self.lesson, self.group))
