"""n.2**n+1 şeklinde yazılabilen doğal sayılara "cullen sayılar" denir.klavyeden girilen
terim sayısı kadar cullen sayılarını listeleyen program."""

GirilenSayı=int(input("Tamsayı giriniz: "))
for i in range(1,GirilenSayı,1):
    print("Cullen sayısının sonucu: ",i*2**i+1)
    