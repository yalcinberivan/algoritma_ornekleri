import math


a=float(input("Birinci kenarı giriniz: "))
b=float(input("İkinci kenarı giriniz: "))
aci=int(input("Aradaki açıyıy giriniz: "))

pi=math.pi
c=a**2+b**2-2*a*b*math.cos(aci*pi/180)**1/2

print("Sonuç: ",c)
