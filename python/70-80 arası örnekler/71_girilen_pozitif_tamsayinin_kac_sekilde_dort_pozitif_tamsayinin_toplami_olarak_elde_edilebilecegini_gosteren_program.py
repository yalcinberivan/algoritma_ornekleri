a=int(input("Pozitif tamsayı giriniz: "))
b=a-3
s=0
for i in range(1,b,1):
    for j in range(i,b,1):
        for k in range(j,b,1):
            for m in range(k,b,1):
                if (i+j+k+m==a):
                    s=s+1
                    print(i,j,k,m)
                    