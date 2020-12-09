h=int(input("Yerden yüksekliği giriniz: "))
vo=int(input("Hızı giriniz: "))

t=(2*h/9*8)**1/2
x=vo*t
vy=9.8*t
v=(vo**2+vy**2)**1/2

print("Geçen süre: {:.3f}\n ".format(t))
print("Cismin hızı: {:.3f}\n ".format(x))
print("Cismin t süre sonraki hızı: {:.3f}\n".format(v))

