import math

print("Kombinasyon(n-r): ")
n=int(input("n: "))
r=int(input("r: "))

f1=math.factorial(n)
f2=math.factorial(r)
f3=math.factorial(n-r)

k=f1/(f2*f3)

print("\nKombinasyon(%d,%d)=%d"%(n,r,k))
