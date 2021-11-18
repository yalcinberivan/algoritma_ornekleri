"""Monte Carlo yöntemi:sayısal sonuçlar elde etmek için tekrarlanan tesadüfi değerlere dayanan hesaplama algoritmaları
olarak özetlenebilir."""
import random
max=random.uniform(1,10)
n=int(input("pozitif tamsayı giriniz: "))
i=1
m=0
for i in range(1,n,1):
    x=(2*random.uniform(1,10))/(random.uniform(1,10)-1)
    y=(2*random.uniform(1,10))/(random.uniform(1,10)-1)
    if(x**2+y**2<1):
        m=m+1
print(4*m/n)
