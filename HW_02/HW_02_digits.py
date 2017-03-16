#1 multiplication 4-number digit
a=6789
s=str(a)
print int(s[0])*int(s[1])*int(s[2])*int(s[3])

#2 swap 2 variables without third
a, b = 1, 2
print 'a=', a, 'b=', b
a, b = b, a
print 'a=', a, 'b=', b
#or
c, d = 1, 2
print 'c=', c, 'd=', d
c += d
d = c-d
c -=d
print 'c=', c, 'd=', d

#3 equation
import math
#a
x = float(input('Input x='))
y = float(input('Input y='))
z = float(input('Input z='))
a= ((math.fabs(x-1.0)**0.5)-(math.fabs(y)**(1.0/3.0)))/(1.0+((x**2.0)/2.0)+((y**2.0)/4.0))
b= x*(math.atan(z)+(math.e**(-(x+3.0))))
print 'A)\na=', a, 'b=', b
#b
a=(3.0+(math.e**(y-1.0)))/(1+(x**2.0)*(math.fabs(y-math.tan(z))))
b=1+math.fabs(y-x)+(((y-x)**2.0)/2.0)+(math.abs((y-x)**3.0)/3.0)
print 'B)\na=', a, 'b=', b
#c
a=((1.0+y)*((x+y)/(x**2.0+4.0)))/(math.e**(-(x)-2.0)+(1.0/(x**2.0+4.0)))
b=(1.0+math.cos(y-2.0))/(((x**4.0)/2.0)+(math.sin(z)**2.0))
#d
a=(y+x)/((y**2.0)+math.fabs(x**2.0/(y+((x**3.0)/3.0))))
b=(1.0+((math.tan(z/2.0))**2))
#e
