"""Dost sayısı:(m,n) tamsayı çifti için; m'nin kendisi hariç tam bölenlerinin toplamı n'ye ve n'nin kendisi hariç
tam bölenlerinin toplamı m'ye eşitse,bu iki sayıya "dost sayısı" denir.klavyeden girilen iki tam sayının,"dost sayılar"
olup olmadığını tespit eden program."""

sayi1=int(input("1.sayıyı giriniz: "))
sayi2=int(input("2.sayıyı giriniz: "))

tsayi1=0
tsayi2=0

for i in range(1,(sayi1-1),1):
    if(sayi1%i==0):
        tsayi1=tsayi1+i
        
for i in range(1,(sayi2-1),1):
    if(sayi2%i==0):
        tsayi2=sayi2+i
        
if(tsayi1==sayi2 and tsayi2==sayi1):
    print("Dost sayılardır...")
    
else:
    print("Dost sayılar değil...")
