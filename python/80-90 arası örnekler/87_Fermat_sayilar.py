"""Fermat sayı:(2**2**n)+1 şeklinde yazılabilen pozitif tamsayılara "fermat sayısı" denir.
klavyeden girilen terim sayısı kadar fermat sayısını listeleyen program."""

GirilenSayı=int(input("Tamsayı giriniz: "))
for i in range(0,GirilenSayı-1,1):
    print("Fermat sayısının sonucu:",2**(2**i)+1)
    