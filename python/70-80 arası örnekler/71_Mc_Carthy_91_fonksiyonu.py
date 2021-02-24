"""bilgisayar bilimcisi john McCarthy tarafından tanımlanan "mc carthy 91 fonksiyonu",aşağıdaki yinelemeli eşitlikle
verilmektedir.buna göre klavyeden girilen değere göre ilgili fonksiyonu hesaplayan program.
m(k)=[ k-10,k>100
     [m(m(k+1)),k<=100"""

def Mc91(k):
    if(k>100):
        return k-10
    else:
        return Mc91(Mc91(k+11))
n=int(input("Değer: "))
print("\nMcCarthy 91 fonksiyon değeri: %d\n"%Mc91(n))