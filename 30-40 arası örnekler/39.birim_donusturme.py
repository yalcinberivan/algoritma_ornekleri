a=eval(input("Uzunluğu giriniz (m): "))

print("\nDönüştürme\n1-mn\n2-cm\n3-dm\n4-km\n")

sec=eval(input("Seçiminiz: "))

if (sec==1):
    b=1000*a
elif (sec==2):
    b=100*a
elif (sec==3):
    b=10*a
elif (sec==4):
    b=a/1000
else:
    b=0

print("\nSonuç: %0.5f"%b)
