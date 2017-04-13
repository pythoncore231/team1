from entity.room import Room
from entity.user import User
from entity.lesson import Lesson
from entity.group import Group
from entity.sheduler import Sheduler

import io

print '\n{:*^50}'.format("ROOMS")

rooms = []
with io.open("in//room.in", 'r') as _file:
    for room in _file:
        if room:
            rooms.append(Room(*room.split()))

for i in rooms:
    print i

with io.open("out//room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")

print '\n{:*^50}'.format("USERS")

users = []
with io.open("in//user.in", 'r') as _file:
    for user in _file:
        if user:
            users.append(User(*user.split()))

for i in users:
    print i

with io.open("out//user.out", 'w') as _file:
    for user in users:
        _file.write(user.to_unicode())
        _file.write(u"\n")

print '\n{:*^50}'.format("LESSONS")

lessons = []
with io.open("in//lesson.in", 'r') as _file:
    for lesson in _file:
        if lesson:
            res = lesson.split()
            for i in users:
                if i.id == res[2]:
                    teacher = i
                    break
            lessons.append(Lesson(id=res[0], name=res[1], teacher=teacher))

for i in lessons:
    print i

with io.open("out//lesson.out", 'w') as _file:
    for lesson in lessons:
        _file.write(lesson.to_unicode())
        _file.write(u"\n")

print '\n{:*^50}'.format("GROUPS")

groups = []
groups.append(Group("231-1PythonCore", [users[0], users[1], users[2]]))
groups.append(Group("231-2PythonCore", [users[3], users[4], users[5]]))

for i in groups:
    print i

with io.open("out//group.out", 'w') as _file:
    for group in groups:
        _file.write(group.to_unicode())
        _file.write(u"\n")

print '\n{:*^50}'.format("SHEDULER")

shedulers = []
shedulers.append(Sheduler(rooms[0], lessons[0], groups[0], 1))
shedulers.append(Sheduler(rooms[1], lessons[1], groups[1], 2))

for i in shedulers:
    print i

with io.open("out//sheduler.out", 'w') as _file:
    for sheduler in shedulers:
        _file.write(sheduler.to_unicode())
        _file.write(u"\n")