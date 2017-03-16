str1 = "arytdgdbvannaeeebbbbiiiiiii"

print(str1.count('a'), str1.count('e'), str1.count('i'))


d = 24544.784245
num = "%f" % d
pos = num.find(".")

print(int(num[pos-3]) + int(num[pos-2]) + int(num[pos-1]) + int(num[pos+1]) + int(num[pos+2]) + int(num[pos+3]))



