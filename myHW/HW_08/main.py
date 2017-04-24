# -*- coding: utf-8 -*-
import io
from entity.room import Room
from entity.user import User
from entity.lesson import Lesson
from entity.group import Group
from entity.sheduler import Sheduler

rooms = []
with io.open("in\\room.in", 'r') as _file:
    for room in _file:
        if room:
            name, capacity = room.split()
            print name, capacity
            rooms.append(Room(name=name, capacity=capacity))
        # _file.write(unicode(i))
        # _file.write(u"\n")
print rooms
for i in rooms:
    print i

with io.open("out\\room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")

pupils = []
with io.open("in\users.in", 'r') as _file:
    for line in _file:
        if line:
            fistname, lastname, age = line.split()
            print fistname, lastname, age
            pupils.append(User(fistname = fistname, lastname = lastname, age = age))

print "pup: ", pupils
for i in pupils:
    print i

with io.open("out\\users.out", 'w') as _file:
    for pupil in pupils:
        _file.write(pupil.to_unicode())
        _file.write(u"\n")

subteach = []
with io.open("in\lessons.in", 'r') as _file:
    for line2 in _file:
        if file:
            name, teacher = line2.split()
            print name, teacher
            subteach.append(Lesson(name = name, teacher = teacher))

print subteach
for i in subteach:
    print i

list_11=[]
list_12=[]

for pupil in pupils:
    if int(pupil.age) % 2:
        list_11.append(pupil)
    else:
        list_12.append(pupil)

group_11 = Group(1, "11", list_11)
group_12 = Group(2, "12", list_12)

groups = [group_11, group_12]

with io.open("out\\group.out", 'w') as _file_group:
    for group in groups:
        _file_group.write(group.to_unicode())
        _file_group.write(u"\n")
        for user in group.members:
            _file_group.write(user.to_unicode())
            _file_group.write(u"\n")

schedulers_11 = (Sheduler(n + 1, rooms[n], subteach[n], groups[0], n + 1) for n in range(7))
schedulers_12 = (Sheduler(n + 8, rooms[n], subteach[n], groups[1], n + 2) for n in range(7))

schedulers = [schedulers_11, schedulers_12]

with io.open("out\\scheduler.out", 'w') as _file_scheduler:
    for schedul in schedulers:
        for each in schedul:
            _file_scheduler.write(each.to_unicode())
            _file_scheduler.write(u"\n")
        for i in schedulers:
            print i
            print i.to_unicode()