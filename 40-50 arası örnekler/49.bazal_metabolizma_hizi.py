k=int(input("Kilonuzu giriniz:  "))
b=int(input("Boyunuzu giriniz: "))
y=int(input("Yaşınızı giriniz: "))
c=str(input("Cinsiyetinizi giriniz: "))

if (c=="E"):
    bmh=66.473+13.7516*k+5.0033*b-6.775*y
    print("bmh=",bmh)
else:
    bmh=655.0955+9.5634*k+1.8496*b-4.6756*y
    print("bmh=",bmh)
