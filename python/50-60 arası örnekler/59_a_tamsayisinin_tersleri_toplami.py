# 2/a=1/x+1/y+1/z ==  x=a,y=a+1,z=a(a+1)
a=int(input("1'den büyük bir sayı giriniz: "))

print("sayının kendisi: ",a)
print("sayinin 1 fazlasi: ",a+1)
print("sayinin bir fazlasının a katı: ",a*(a+1))

print("sayinin terslerinin toplami: {:.2f} ".format(2/a))
