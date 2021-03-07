"""John Wallis:klavyeden girilen terim sayısı kadar çarpım yaparak,
pi sayısını hesaplayan ve ekranda gösteren program."""
n=int(input("Terim sayısını giriniz: "))
c=1
k=1
for k in range(1,n,1):
    c1=4*k*k
    c=c*c1/(c1-1)
print(2*c)
