n=int(input("Pozitif tamsayı giriniz: "))

t1=t2=t3=0

for i in range (1,n+1):
    t1+=i
    t1=sum(range(1,n+1,1))

for i in range (1,n+1,2):
    t2+=i
    t2=sum(range(1,n+1,2))

for i in range (2,n+1,1):
    t3+=i
    t3=sum(range(2,n+1,2))

print("\n1'den %d'ye kadar sayıların toplamı (birer-birer): "%n,t1)
print("1'den %d'ye kadar sayıların toplamı (üçer-üçer): "%n,t2)
print("2'den %d'ye kadar sayıların toplamı (ikişer ikişer): "%n,t3)
