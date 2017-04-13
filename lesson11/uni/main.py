import io
from entity.room import Room


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
