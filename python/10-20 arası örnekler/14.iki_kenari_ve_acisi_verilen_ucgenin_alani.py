import math


a=eval(input("Birinci kenarı giriniz (cm) :"))
b=eval(input("İkinci kenarı giriniz (cm) : "))
aci=eval(input("Aradaki açıyı giriniz (derece) : "))

alan=a*b*math.sin(math.radians(aci))/2

print("\nÜçgenin alanı (cm2) : {:.2f}\n".format(alan))
