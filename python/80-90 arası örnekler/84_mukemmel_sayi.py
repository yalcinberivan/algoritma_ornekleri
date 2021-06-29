#Mükemmel Sayı:kendisi hariç bütün pozitif tamsayı çarpanları(tam bölenleri)toplamı,yine kendisine eşit olan 
#sayılara "mükemmel sayı" denir

GirilenSayi=int(input("Tamsayı giriniz: "))
t=0
for i in range(1,GirilenSayi):
    if(GirilenSayi%i==0):
        t+=i
if (GirilenSayi==t):
    print("Mükemmel sayı....")
else:
    print("Mükemmel sayı değil...")