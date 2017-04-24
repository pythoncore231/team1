import io
from entity.room import Room
from entity.user import User
from entity.scheduler import Scheduler
from entity.lesson import Lesson
from entity.group import Group

rooms = []
with io.open("in//room.in", 'r') as _file:
    for room in _file:
        if room:
            id, name, capacity = room.split()
            rooms.append(Room(id=id, name=name, capacity=capacity))
print rooms
for i in rooms:
    print i

with io.open("out//room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")


print "-" * 60
users = []
with io.open("in//user.in", 'r') as _file:
    for user in _file:
        if user:
            id, firstname, lastname, age = user.split()
            users.append(User(id=id, firstname=firstname, lastname=lastname, age=age))
print users
for i in users:
    print i

with io.open("out//user.out", 'w') as _file:
    for user in users:
        _file.write(user.to_unicode())
        _file.write(u"\n")




print "-" * 60
groups = []
with io.open("in//group.in", 'r') as _file:
    for group in _file:
        if group:
            id, name, members = group.split()
            groups.append(Group(id=id, name = name, members = members))
print groups
for i in groups:
    print i

with io.open("out//group.out", 'w') as _file:
    for group in groups:
        _file.write(group.to_unicode())
        _file.write(u"\n")



print "-" * 60
lessons = []
with io.open("in//lessons.in", 'r') as _file:
    for lesson in _file:
        if lesson:
            id, name, teacher = lesson.split()
            lessons.append(Lesson(id=id, name = name, teacher = teacher))
print lessons
for i in lessons:
    print i

with io.open("out//lessons.out", 'w') as _file:
    for lesson in lessons:
        _file.write(lesson.to_unicode())
        _file.write(u"\n")



print "-" * 60
schedulers = []
with io.open("in//scheduler.in", 'r') as _file:
    for scheduler in _file:
        if scheduler:
            room, lesson, group, id = scheduler.split()
            schedulers.append(Scheduler(room=room, lesson=lesson, group=group, id=id))
print schedulers
for i in schedulers:
    print i

with io.open("out//scheduler.out", 'w') as _file:
    for scheduler in schedulers:
        _file.write(scheduler.to_unicode())
        _file.write(u"\n")
