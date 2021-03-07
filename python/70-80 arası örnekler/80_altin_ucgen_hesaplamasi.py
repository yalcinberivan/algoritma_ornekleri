"""altın üçgen:uzun kenarları eşit ve bu kenarlardan birinin,kısa kenara oranı;
altın orana eşit olan ikizkenar üçgenlere altın üçgen denir.klavyeden kısa kenarı
girilen altın üçgenin tüm kenarlarını yazdıran program."""

a=int(input("kısa kenarı giriniz: "))
b=a*(1+5**(1/2))/2
print("A kenarının uzunluğu:{:.2f}\n".format(a))
print("B kenarının uzunluğu:{:.2f}\n".format(b))
