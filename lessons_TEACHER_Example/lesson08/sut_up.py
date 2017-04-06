# import fibo

# print fibo.fibo1(7)
# print fibo.fibo2(7)

# import fibo as fib

# print fib.fibo1(7)
# print fib.fibo2(7)
# print dir()
# print type(fib)

# from fibo import fibo1

# print fibo1(5)
# print dir()
# print type(fibo1)

# import mat
# import sys

# print sys.path
# for i in sys.path:
#     print i
# sys.path.append('D:\\test\\team1\\lesson08\\pac')
# print sys.path
# for i in sys.path:
#     print i

# from pac import mat
# print mat.pow(2,8)

# from pac.sub_pac import math1

# print math1.sqrt(9)
# from pac.sub_pac.math2 import abs
# print abs(-12)
# print abs(12)
# from fibo import fibo1 as f1, CONST as c, fibo2 as f2
import fibo

f1 = lambda a: a*a

print f1(8)
print fibo.fibo1(8)
# print c