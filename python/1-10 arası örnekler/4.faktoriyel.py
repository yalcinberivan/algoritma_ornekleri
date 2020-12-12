sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
deger = 1
for i in range(1, sayi+1):
    deger = deger * i
    
print("Faktoriyel : ", deger)
