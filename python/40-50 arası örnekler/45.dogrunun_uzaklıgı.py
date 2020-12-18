
a=int(input("X'in katsayısını giriniz: "))
b=int(input("Y'nin katsayısını giriniz: " ))
c=int(input("Sabiti giriniz: "))
x1=int(input("X1 noktasını giriniz: "))
y1=int(input("X2 noktasını giriniz: "))

if (a*x1+b*y1+c==0):
    print("Girilen nokta,doğru üzerindedir.")
uz=abs(a*x1+b*y1+c)/(a**2+b**2)**(1/2)
print("Girilen nokta,doğrunun üzerinde değildir.Noktanın,doğruya uzaklığı",uz,"birimdir.")
