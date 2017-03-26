#Find the sum of the cubes digits natural number.
number = input(" Enter your cube number : ")
lenght = len(str(number))
summy = 0
for i in range(lenght):
	cube = int(str(number)[i]) ** 3
	summy += cube
print summy
a = '45sfsfsfsf'
print int(str(a[0]))  + int(str(a[1]))
