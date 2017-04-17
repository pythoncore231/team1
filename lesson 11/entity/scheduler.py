# -*- coding: utf-8 -*-
from base import Base


class Scheduler(Base):
    def __init__(self, id=0, room=None, lesson=None, group=None, para=None):
        super(Scheduler, self).__init__(id)
        self.room = room
        self.lesson = lesson
        self.group = group
        self.para = para

    def __str__(self):
        return "id:{} room:{} lesson:{} group:{} para:{}".format(self.id, self.room, self.lesson, self.group, self.para)

    def __repr__(self):
        return "{}".format(self.room)

    def to_unicode(self):
        return unicode("<{}> <{}> <{}> <{}> <{}>".
                       format(self.id, self.room, self.lesson, self.group, self.para))
