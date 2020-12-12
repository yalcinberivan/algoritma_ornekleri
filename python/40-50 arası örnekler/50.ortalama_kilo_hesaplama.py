
girilenKilo=input("Kilonuzu giriniz: ")
girilenBoy=input("Boyunuzu giriniz: ")
girilenYontem=input('Lütfen yöntemi giriniz: ')




if girilenKilo != '' or girilenBoy != '' or girilenYontem != '':
    
    k=float(girilenKilo)
    b=float(girilenBoy)
    y=int(girilenYontem)
    
    c=''

    if y == 1 or y == 2 :
        c=str(input("Cinsiyetinizi giriniz: "))


    def yontem1(k,b,c):
        bki=0
        if c == 'e':
            bki=50+2.3*(b/2.54-60)
        else:
            bki=45.5+2.3*(b/2.54-60)
        print("ideal boy kilo oranınız: ",bki)
        
        
    yas=''

    if y == 2:
        yas=int(input("Yaşınızı giriniz: "))

    def yontem2(k,b,c,yas):
        bki=0
        if c == 'e':
            bki=(b-100+yas/10)*0.9
        else:
            bki=(b-100+yas/10)*0.8
        print("İdeal boy kilo oranınız: ",bki)
        
        
    def yontem3(k,b):
        bki=k/(b*b)
        if (bki<=17.5):
            print("Anoreksi,aşırı zayıf,yüksek risk")
        elif ((bki>17.5) and (bki<20.7)):
            print("Zayıf")
        elif ((bki>=20.7) and (bki<26.4)):
            print("Normal kilolu")
        elif ((bki>=26.4) and (bki<27.8)):
            print("Biraz fazla kilolu")
        elif ((bki>=27.8) and (bki<31.1)):
            print("Fazla kilolu")
        elif ((bki>=31.1) and (bki<34.9)):
            print("Çok fazla kilolu")
        elif ((bki>=35) and (bki<40)):
            print("Sağlık açısısndan yüksek riskli kilolu")
        elif ((bki>=40) and (bki<50)):
            print("Hastalıklı bir şekilde kilolu")
        else:
            print("Süper aşırı kilolu")
            
        
        
        
    def yontem4(b,k):
        bki=k/(b*b)
        if (bki<18.5):
            print("Zayıf")
        elif ((bki>=18.5) and (bki<25)):
            print("Orta")
        elif ((bki>=25) and (bki<30)):
            print("Fazla kilolu")
        elif ((bki>=30) and (bki<35)):
            print("1.derece obez")    
        elif ((bki>=35) and (bki<40)):
            print("2.derece obez")
        else:
            print("3.derece morbid obez")
            


    if y == 1:
        yontem1(k, b, c)
    if y == 2:
        yontem2(k, b, c, yas)
    if y == 3:
        yontem3(k, b,)
    if y == 4:
        yontem4(b, k)
else:
    print("Lütfen girdiğiniz değerleri kontrol ediniz!!!")
