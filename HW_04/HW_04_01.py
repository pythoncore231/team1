#Find all Four digit numbers, which tsyfer amount equal to a given number

number = 20
for i in range(10**3, 10**4):
   temp = i/1000 + (i/100)%10 + (i%100)/10 + i%10
   if temp == number:
           print temp



print range(10**3, 10**4)

N = 4567 
x___ = i/1000 
_x__ = (i/100)%10# xx__ => _x__ 
__x_ = (i%100)/10# __xx => __x_
___x = i%10
