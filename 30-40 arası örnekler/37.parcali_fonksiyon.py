x=eval(input("x noktasını giriniz: "))

if (x<0):
    y=1
elif ((0<=x) and (x<=2)):
    y=x
elif ((2<x) and (x<=4)):
    y=3
else:
    y=4-x
    
print("Fonksiyonun x=%0.2f noktasındaki değeri=%0.2f\n"%(x,y))
