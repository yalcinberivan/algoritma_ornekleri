print("Belirtilen aralıktaki ASAL sayılar\n ")
n=int(input("Üst sınır: "));
print("\n++++ ASAL SAYILAR ++++\n");
for i in range(2,n+1):
    s=0
    for j in range(1,i+1):
        if(i%j==0):
            s=s+1
    if (s==2):
        print("%d\t"%i,end=" ")
        