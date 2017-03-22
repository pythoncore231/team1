# 1 count of words in text
string = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts."""
str2 = "co"

count = 0
for i in string.lower().split():
    start = i.find(str2)
    if start == 0:
        count += 1
print count