"""Leyland sayı:x>1 ve y>1 tamsayıları için x**y+y**x elde edebilen sayılara leyland sayıları denir.
ilk 7 leyland sayısı 8,17,32,54,57,100 ve 145'tir.Klavyeden girilen x ve y değerleri için mümkün olan tüm leyland 
sayılarını hesaplayıp ekrana yazdıran program."""

#sayi1=x
#sayi2=y

sayi1=int(input("1.sayıyı giriniz: "))
sayi2=int(input("2.sayıyı giriniz: "))
for i in range(2,sayi1,1):
    for j in range(2,sayi2,1):
        print("Leyland sayısının sonucu: ",i**j+j**i)
