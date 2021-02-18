b=int(input("Tamsayı giriniz: ")) 
for a in range(99):
    if (a**3-a**2==b):
        print("%d sayısı 0 ile 100 arasındadır."%a)
        break
else:
    print("0-100 arasında öyle bir sayı yok...")