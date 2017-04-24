from base import Base

class Sheduler(Base):
    def __init__(self, id = 0, room = None, lesson = None, group = None, para = None):
        super(Sheduler, self).__init__()
        self.id = id
        self.room = room
        self.lesson = lesson
        self.group = group
        self.para = para

    def __str__(self):
        return "id:{} room:{} lesson: {} group: {} para: {}".format(self.id, self.room,self.room,self.lesson,self.group,self.para)
    def __unicode__(self):
        return unicode("{} {} {} {} {} {}".format(self.id, self.room,self.room,self.lesson,self.group,self.para))
    def to_unicode(self):
        return self.__unicode__()