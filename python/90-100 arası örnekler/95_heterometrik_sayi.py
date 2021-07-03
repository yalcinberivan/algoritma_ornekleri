"""Heterometrik sayı:a pozitif bir tamsayı olmak üzere a(a+1) ile elde edilebilen sayılara "heterometrik sayı" denir
ör:2=1.2,6=2.3,12=3.4 bu sayılardan bazılarıdır"""
#klavyeden girilen adet sayısınca "heterometrik sayıları oluşturan ve bunları açık yazarak alt alta listeleyen program. 

sayi=int(input("Tamsayı giriniz: "))
for a in range (1,sayi,1):
    print(a,"x",a+1,"=",a*(a+1))
    
