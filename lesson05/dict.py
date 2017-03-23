d = dict()
d = {1:1,
     1:"dasf",
     "a":"sda",
     "a": [ {1:1, 1:"dasf", "a":"sda", "a":{1:1, 1:"dasf", "a":"sda", "a":1}}]}
print d, type(d)
s = set()
print {1,2,3,4,1,2,3,21,3,54,2,4,54} - {1,2,3}
print {1,2,3,4,1,2,3,21,3,54,2,4,54,"as", "st"} | {1,2,3,99,"st"}
print s, type(s)
print dir(d)
l = [1,2,3,4]
k = l[:]
ss = d.copy()
print ss["a"]
ss["test"]= dict(a=1, b=2) #{"a":1, "b":2}
print ss
ss.setdefault("!!!")
ss.setdefault("!!!",11)
# print ss.get("Test"), ss.get("test")
# print ss.keys()
# for i in ss:
#     print "key:{} \tvalue:{}".format(i , ss[i])
# for key, value in d.iteritems():
#     print "key:{} \tvalue:{}".format(key , value)
print ss.pop("a")
print ss
print ss.popitem()

def f(a=0, b=0, c=0):
    print a, b, c
    return a+b+c

d ={"a":10, "b":20, "c":30}
t = (1,2,3)
print f(c = d["a"], b = d["b"],a = d["c"])
print f(**d)
print f(t[0], t[1], t[2])
print f(*t)
