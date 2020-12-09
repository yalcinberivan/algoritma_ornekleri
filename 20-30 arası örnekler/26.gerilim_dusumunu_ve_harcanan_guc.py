e=int(input("Gerilimi giriniz: "))

r1=int(input("Birinci direnci giriniz: "))
r2=int(input("İkinci direnci giriniz: "))
r3=int(input("Üçüncü direnci giriniz: "))
r4=int(input("Dördüncü direnci giriniz: "))

i=e/(r1+r2+r3+r4)
vr1=r1*i
pr2=i**2*r2

print("Devreden akan akım: {:.2f}\n ".format(i))
print("R1 direncinde harcanan güç: {:.2f}\n ".format(vr1))
print("R2 direncinde harcanan güç: {:.2f}\n ".format(pr2))
