a=int(input("Pozitif tamsayı giriniz: "))
print("%d tamsayısının tam bölenleri: "%a)

for i in range(1,a+1):
    if (a%i==0):
        print("%d"%i)

