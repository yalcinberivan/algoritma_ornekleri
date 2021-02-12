t=0
i=0
n=int(input("sayiyi gir: "))

for i in range(n):
    s=int(input("sayi gir: "))
    t=t+(s%10)
print("Sayinin birler basamaklari toplami: ",t)
