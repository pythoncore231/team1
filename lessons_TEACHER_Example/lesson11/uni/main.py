import io
from entity.room import Room


rooms = []
with io.open("in\\room.in", 'r') as _file:
    for room in _file:
        if room:
            id, name, capacity = room.split()
            rooms.append(Room(id=id, name=name, capacity=capacity))
        # _file.write(unicode(i))
        # _file.write(u"\n")
print rooms
for i in rooms:
    print i

with io.open("out\\room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")
        