"""Ore sayısı:1,6,28,140,270,496 gibi tam bölenlerinin harmonik ortalaması tamsayı olan pozitif tamsayılara "harmonik bölücü sayısı
" veya "ore sayısı"denir.
ör:28 tamsayısının bölenleri 1,2,4,7,14,28 olduğundan bunların harmonik ortalaması 6/(1/1+1/2+1/4+1/7+1/14+1/28)=3
olup tamsayıdır bu nedenle 28 bir "ore sayısı" dır"""

a=int(input("Sayıyı giriniz: "))
s=0; t=0;
for i in range (1,a,1):
    if(a%i==0):
        s=s+1; t=t+1;
    ho=s/t
if(ho==round(ho)):
    print("Ore sayıdır...")