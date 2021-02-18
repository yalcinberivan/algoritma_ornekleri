pay=int(input("Payı giriniz: "))
payda=int(input("Paydayı giriniz: "))

bolum=0
kalan=pay

while (kalan>=payda):
    kalan=kalan-payda
    bolum=bolum+1
    
print("Bölüm: ",bolum)
print("Kalan:",kalan)
