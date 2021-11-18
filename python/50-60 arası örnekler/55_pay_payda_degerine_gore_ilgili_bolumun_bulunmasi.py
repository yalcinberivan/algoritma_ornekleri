i=1
a=int(input("a sayisini gir: "))
b=int(input("b sayisini gir: "))
n=int(input("n sayisini gir: "))
for i in range(n):
    a=10*a
    c=int(a/b)
    a=a%b
print("x:",c)
