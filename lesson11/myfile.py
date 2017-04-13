import io
l = io.open("data.dat", 'r', encoding='utf-8') 
for line in l:
    print line

l.close()
print "*"*55
with io.open("data.dat", 'r') as _file:
    for line in _file:
        print type(line)
        print line    

with io.open("out.dat", 'w+') as _file:
    for i in range(10):
        _file.write(unicode(i))
        _file.write(u"\n")

