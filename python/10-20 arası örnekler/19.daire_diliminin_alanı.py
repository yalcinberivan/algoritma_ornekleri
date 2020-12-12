import math

r=int(input("Yarıçapı giriniz: "))
aci=int(input("Açıyı giriniz: "))

pi=math.pi
alan=(aci*pi*r**2)/360

print("Daire diliminin alanı: {:.2f}\n".format(alan))
