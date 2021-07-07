a=int(input("Pozitif tamsayı giriniz: "))
t=0; s=0;
for i in range (1,a,1):
    if(a%i==0):
        t=t+i; s=s+1;
if (t/s==int(t/s)):
    print("aritmetik sayıdır...")
else:
    print("aritmetik sayı değildir...")