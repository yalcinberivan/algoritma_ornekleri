"""madhava of sangamagrama:seri toplmamıyla hesaplanabilmektedir.
buna göre klavyeden girilen terim sayısı için pi değerini hesaplar."""

n=int(input("Terim sayısını giriniz: "))
t=0
k=0
for k in range(n,-1,1):
    t=t+(-1)**k/((2*k+1)*3**k)
    break
print("girilen terim sayısına göre pi değeri:",12**(1/2)*t)