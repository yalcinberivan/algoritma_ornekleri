"""Bağdaşık sayı:iki basamaklı iki doğal sayının birler basamağındaki rakamların toplamı 10 ve onlar
basamağındaki rakamlar aynı ise bu iki doğal sayıya "bagdaşık sayılar" denir."""
#klaveden girilen 2 doğal sayının bağdaşık olup olmadığını bulan program. 

a=int(input("1.sayıyı giriniz: "))
b=int(input("2.sayıyı giriniz: "))

a1=int(a/10); a2=(a%10)
b1=int(b/10); b2=(b%10)

if((a1==b1) and (a2+b2==10)):
    print("Girilen sayılar bağdaşık sayıdır")
else:
    print("Girilen sayı bağdaşık sayı değildir")
    
