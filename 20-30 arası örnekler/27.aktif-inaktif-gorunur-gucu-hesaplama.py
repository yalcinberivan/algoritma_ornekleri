import math


v=int(input("Akımın volt cinsinden faz açısını giriniz: "))
i=int(input("Akımın amper cinsinden faz açısını giriniz: "))
fi=int(input("Akımın derece cinsinden faz açısını giriniz: "))

pi=math.pi
fi=fi*pi/180
s=v*i
gf=math.cos(fi)
p=s*gf
q=s*math.sin(fi)

print("Akımın aktif gücü: {:.3f}\n ".format(p))
print("Akımın reaktif gücü: {:.3f}\n ".format(q))
print("Akımın görünür gücü: {:.3f}\n ".format(s))
print("Akımın güç faktörü: {:.3f}\n".format(gf))
