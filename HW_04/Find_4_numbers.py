'''
Created on Mar 17, 2017

@author: vodachuk
'''
n = input("Enter the number : ")

num = range(1000, 10000)

for i in num:
    if (int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])) == n:
        print i