n=int(input("Bir tamsayı giriniz: "))
enb=-1
i=1 
for i in range(n):
    a=int(input("Bir tamsayı giriniz: "))
    if (a%2==0 and a>enb):
        enb=a
    else:
        print("x: ",enb)
