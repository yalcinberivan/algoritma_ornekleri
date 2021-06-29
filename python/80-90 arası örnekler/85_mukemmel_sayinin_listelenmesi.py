GirilenSayi=int(input("Tamsayı giriniz: "))
for i in range(1,GirilenSayi,1):
    a=2**i
    b=2**(i+1)
if GirilenSayi > 1:
    for i in range(2,GirilenSayi):
        if (GirilenSayi % i) == 0:
            print(GirilenSayi," Asal Sayı Değildir.")
        break
    else:
        print(GirilenSayi," Asal Sayıdır.\n",a*b)
    