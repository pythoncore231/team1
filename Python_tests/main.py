'''
Created on Apr 13, 2017

@author: vodachuk
    
    Read data from files about rooms, users
    Create two groups and add users there, after that wrote the result to file
    
'''
import io
from entity.room import Room
from entity.user import User
from entity.lesson import Lesson

# ============================ Rooms ============================= 
rooms = []
with io.open("in//room.in", "r") as _file:
    for room in _file:
        if room:
            id, name, capacity = room.split()
            print name, capacity
            rooms.append(Room(id = id, name = name, capacity = capacity))
            
print rooms
for i in rooms:
    print i

with io.open("out//room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")
# ============================ Users =============================       
users = []
with io.open("in//user.in", "r") as _file_user:
    for user in _file_user:
        if user:
            id, FirstName, LastName, age = user.split()
            print FirstName, LastName, age
            users.append(User(id = id, FirstName = FirstName, LastName = LastName, age = age))
            
print users
for i in users:
    print i

with io.open("out//user.out", 'w') as _file_user:
    for user in users:
        _file_user.write(user.to_unicode())
        _file_user.write(u"\n")
# ============================ Lessons =============================  
lessons = []
with io.open("in//lesson.in", "r") as _file_lesson:
    for lesson in _file_lesson:
        if lesson:
            id, name, teacher = lesson.split()
            print name, teacher
            lessons.append(Lesson(id = id, name = name, teacher = teacher))
#             if lesson == Lesson.teacher:
#                 teacher = lesson.split()
#                 print teacher
#                 lessons.append(Lesson(teacher = teacher))
            
print lessons
for i in lessons:
    print i

with io.open("out//lesson.out", 'w') as _file_lesson:
    for lesson in lessons:
        _file_lesson.write(lesson.to_unicode())
        _file_lesson.write(u"\n")










