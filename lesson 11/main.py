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

scheduler_101_1 = Scheduler(1, rooms[0], lessons[0], groups[0], 1)
scheduler_101_2 = Scheduler(2, rooms[1], lessons[1], groups[0], 2)
scheduler_101_3 = Scheduler(3, rooms[2], lessons[2], groups[0], 3)
scheduler_101_4 = Scheduler(4, rooms[3], lessons[3], groups[0], 4)
scheduler_101_5 = Scheduler(5, rooms[4], lessons[4], groups[0], 5)
scheduler_101_6 = Scheduler(6, rooms[5], lessons[5], groups[0], 6)
scheduler_101_7 = Scheduler(7, rooms[6], lessons[6], groups[0], 7)

scheduler_202_1 = Scheduler(8, rooms[6], lessons[6], groups[1], 1)
scheduler_202_2 = Scheduler(9, rooms[5], lessons[5], groups[1], 2)
scheduler_202_3 = Scheduler(10, rooms[4], lessons[4], groups[1], 3)
scheduler_202_4 = Scheduler(11, rooms[2], lessons[2], groups[1], 4)
scheduler_202_5 = Scheduler(12, rooms[3], lessons[3], groups[1], 5)
scheduler_202_6 = Scheduler(13, rooms[1], lessons[1], groups[1], 6)
scheduler_202_7 = Scheduler(14, rooms[0], lessons[0], groups[1], 7)

schedulers_101 = [scheduler_101_1, scheduler_101_2, scheduler_101_3, scheduler_101_4,
                  scheduler_101_5, scheduler_101_6, scheduler_101_7]

schedulers_202 = [scheduler_202_1, scheduler_202_2, scheduler_202_3, scheduler_202_4,
                  scheduler_202_5, scheduler_202_6, scheduler_202_7]

schedulers = [schedulers_101, schedulers_202]

with io.open("out\\scheduler.out", 'w') as _file_scheduler:
    for schedul in schedulers:
        for each in schedul:
            _file_scheduler.write(each.to_unicode())
            _file_scheduler.write(u"\n")
