#Find all Four digit numbers, which tsyfer amount equal to a given number

number = "20"
for i in range(10**3, 10**4):
   temp = i/1000 + (i/100)%10 + (i%100)/10 + i%10
   if temp == number:
           print temp
           