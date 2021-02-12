a=int(input("Sayiyi gir: "))
ort=0
if(a>99) or (a<999):
    bir=a%10
    on=(int(a/10))%10
    yuz=int(a/100)
    ort=(bir+on+yuz)/3
print("Sayinin ortalamasi: ",ort)
