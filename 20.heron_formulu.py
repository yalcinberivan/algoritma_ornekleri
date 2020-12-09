a=int(input("Birinci kenarı giriniz: "))
b=int(input("İkinci kenarı giriniz: "))
c=int(input("Üçüncü kenarı giriniz: "))
u=(a+b+c)/2
alan=(u*(u-a)*(u-b)*(u-c))**1/2
print("Alan: {:.2f}\n".format(alan))
