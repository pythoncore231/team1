import io
from entity.room import Room
from entity.user import User
from entity.lesson import Lesson
# from entity.group import Group


# rooms = []
# with io.open("in\\room.in", 'r') as _file:
#     for room in _file:
#         if room:
#             id, name, capacity = room.split()
#             rooms.append(Room(id=id, name=name, capacity=capacity))
#         # _file.write(unicode(i))
#         # _file.write(u"\n")
# 
# with io.open("out\\room.out", 'w') as _file:
#     for room in rooms:
#         _file.write(room.to_unicode())
#         _file.write(u"\n")

users=[]
with io.open('in\\users.in', 'r') as _file:
    for user in _file:
        if user:
            firstname, lastname, age = user.split()
            users.append(User(firstname=firstname, lastname=lastname, age=age))

# print users
# for user in users:
#     print user
# with io.open('out\\users.out', 'w') as _file:
#     for user in users:
#         _file.write(user.to_unicode())
#         _file.write(u'\n')

# lessons=[]
# with io.open('in\\lesson.in', 'r') as _file:
#     for lesson in _file:
#         if lesson:       ### equal lessons.append(Lesson(*lesson.split()))
#             name, teacher = lesson.split()
#             lessons.append(Lesson(name=name, teacher=teacher))

# print lessons
# print lessons[0], lessons[3]
# for lesson in lessons: ####WTF it knows 'lessons' is instance of class????
#     print lesson

# with io.open('out\\lesson.out', 'w') as _file:
#     for lesson in lessons:
#         _file.write(lesson.to_unicode())
#         _file.write(u'\n')

l=len(users)
group={}
print help(dict)
ls = ['1', 2, 3, '4']
st = ('a', 'b', 'c', 'd')
# print dir(group)
# group.setdefault('group1', 'group2')
print group