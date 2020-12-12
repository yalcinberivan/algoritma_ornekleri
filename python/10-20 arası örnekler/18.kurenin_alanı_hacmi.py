import math


r=int(input("Yarıçapı giriniz: "))

pi=math.pi
alan=4*pi*r**2
hacim=(4*pi*r**3)/3

print("Kürenin hacmi: {:.2f}\n ".format(hacim))
print("Kürenin alanı: {:.2f}\n".format(alan))