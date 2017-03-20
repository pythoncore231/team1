'''
Created on Mar 17, 2017

@author: vodachuk
'''
N = input("Enter N: ")
k, f = 0, 1
for i in range(N):
    print f
    k, f = f, k + f