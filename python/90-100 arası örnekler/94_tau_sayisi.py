"""Tau sayısı:1,2,8,9,12,18,24,36,40,56.... gibi tam bölenlerinin sayısına tam bölünebilen tamsayılara "tau sayısı"
denir.ör:18'in tam bölenleri 1,2,3,6,9 ve 18 olup 6 adettir ve 18,6'ya tam bölünebilmektedir."""
#klavyeden girilen üst sınıra kadar olan tau sayılarını listeleyen program.

ustSınır=int(input("Üst sınırı giriniz: "))
for i in range (1,ustSınır+1,1):
    s=0
    for j in range(1,i+1,1):
        if(i%j==0):
            s=s+1
    if(s>0 and i%s==0):
        print(i)
    