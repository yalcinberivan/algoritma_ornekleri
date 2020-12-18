m=int(input("Maddenin kütlesini giriniz (m) : "))
v=int(input("Maddenin hızını giriniz (v) :"))
h=int(input("Yüksekliği giriniz (h) :"))

yerCekimSabiti = 9.8
ep=m*yerCekimSabiti*h
ek=(m*v**2)/2

print("potansiyel enerji: ",ep)
print("Kinetik enerji: ",ek)
