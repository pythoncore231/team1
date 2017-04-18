# -*- coding: utf-8 -*-
import io
from entity.room import Room
from entity.lesson import Lesson
from entity.User import User
from entity.group import Group
from entity.scheduler import Scheduler


# зчитати дані з файлів про кімнати, предмети, користувачів,
rooms = []
with io.open("in\\room.in", 'r') as _file_room:
    for room in _file_room:
        if room:
            id, name, capacity = room.split()
            rooms.append(Room(id=id, name=name, capacity=capacity))
        # _file_room.write(unicode(i))
        # _file_room.write(u"\n")

with io.open("out\\room.out", 'w') as _file_room:
    for room in rooms:
        _file_room.write(room.to_unicode())
        _file_room.write(u"\n")

lessons = []
with io.open("in\\lesson.in", 'r') as _file_lesson:
    for lesson in _file_lesson:
        if lesson:
            id, name, teacher = lesson.split()
            lessons.append(Lesson(id=id, name=name, teacher=teacher))

with io.open("out\\lesson.out", 'w') as _file_lesson:
    for lesson in lessons:
        _file_lesson.write(lesson.to_unicode())
        _file_lesson.write(u"\n")

users = []
with io.open("in\\User.in", 'r') as _file_user:
    for user in _file_user:
        if user:
            id, first_name, last_name, age = user.split()
            users.append(User(id=id, first_name=first_name, last_name=last_name, age=age))
            # _file_user.write(unicode(i))
            # _file_user.write(u"\n")

with io.open("out\\User.out", 'w') as _file_user:
    for user in users:
        _file_user.write(user.to_unicode())
        _file_user.write(u"\n")


# створити дві групи і заповнити користувачами, після чого записати результат у файл

list_101 = []
list_202 = []

for user in users:
    if int(user.id) % 2:
        list_101.append(user)
    else:
        list_202.append(user)

group_101 = Group(1, "101", list_101)
group_202 = Group(2, "202", list_202)

groups = [group_101, group_202]

with io.open("out\\group.out", 'w') as _file_group:
    for group in groups:
        _file_group.write(group.to_unicode())
        _file_group.write(u"\n")


# на основі вже сформованих даних сформувати довільний розклад і записати у відповідний файл
# scheduler.py: room, lesson, group, para (1,2,3 int)

schedulers_101 = (Scheduler(n + 1, rooms[n], lessons[n], groups[0], n + 1) for n in range(7))
schedulers_202 = (Scheduler(n + 8, rooms[n], lessons[n], groups[1], n + 2) for n in range(7))

schedulers = [schedulers_101, schedulers_202]

with io.open("out\\scheduler.out", 'w') as _file_scheduler:
    for schedul in schedulers:
        for each in schedul:
            _file_scheduler.write(each.to_unicode())
            _file_scheduler.write(u"\n")
