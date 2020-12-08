import math
e=float(input("Birinci köşegeni giriniz: "))
f=float(input("İkinci köşegeni giriniz: "))
aci=int(input("Aradaki açıyı giriniz: "))
pi=3.14
alan=e*f*math.sin(aci*pi/180)/2
print("Dörtgenin alanı: {:.2f}\n ".format(alan))