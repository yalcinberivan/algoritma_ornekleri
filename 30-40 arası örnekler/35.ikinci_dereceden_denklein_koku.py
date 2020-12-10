import math
import cmath


print("Ax^+Bx+C=0")

a=eval(input("A= "))
b=eval(input("B= "))
c=eval(input("C= "))

d=b**2-4*a*c

if (d>=0):
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
else:
    x1=(-b-cmath.sqrt(d))/(2*a)
    x2=(-b+cmath.sqrt(d))/(2*a)
    
print("\nKökler: ")
print(x1,x2,sep='\n')
