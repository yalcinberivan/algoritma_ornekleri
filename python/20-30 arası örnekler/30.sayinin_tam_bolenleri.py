sayi=int(input("Pozitif tamsayı giriniz: "))

print("%d tamsayısının tam bölenleri: "%sayi)

for i in range(1,sayi+1):
    if (sayi%i==0):
        print("%d"%i)
