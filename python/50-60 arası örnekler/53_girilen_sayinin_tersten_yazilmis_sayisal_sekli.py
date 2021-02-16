a=int(input("Sayiyi gir: "))
b=0
while(a>0):
    k=a%10
    b=b*10+k
    a=int(a/10)
    print("Girilen sayinin sayisal degeri: ",b)
