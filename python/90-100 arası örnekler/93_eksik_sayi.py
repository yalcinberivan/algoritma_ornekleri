#klavyeden girilen bir tamsayının "eksik sayı" olup olmadığını,eksik sayı ise eksiklik miktarını ekrana yazan program.
"""ör:15 sayısının tam bölenleri 1,3,5,15 olup bunların toplamı 24 tür tam bölenlerinin toplamı,sayının iki
katından küçük olup (24<30) eksiklik miktarı 6'dır."""

s=int(input("Sayıyı giriniz: "))
t=0
for i in range(1,s+1,1):
    if(s%i==0):
        t=t+i
if(t<2*s):
    print("Eksik sayıdır ve eksiklik miktarı = ",2*s-t)
    