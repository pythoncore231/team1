'''
Created on Mar 16, 2017

@author: vodachuk
'''
k = input("Enter k in range 1 to 365: ")
mas = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
n = k % 7
if n == 1:
    print mas[0]
elif n == 2:
    print mas[1]
elif n == 3:
    print mas[2]
elif n == 4:
    print mas[3]
elif n == 5:
    print mas[4]
elif n == 6:
    print mas[5]
elif n == 7:
    print mas[6]