n=int(input("bölüm sayısını giriniz: "))
t=1
i=1
for i in range(1,n,-1):
    t=1+1/(2+1/t)
print(1+1/t)
