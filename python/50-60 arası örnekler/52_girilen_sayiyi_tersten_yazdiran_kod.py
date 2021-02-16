sayi = int(input("Sayıyı Gir : "))    
ters = 0    
while(sayi > 0):    
    gecici = sayi %10    
    ters = (ters *10) + gecici    
    sayi = sayi //10    
     
print("Sayının Ters Çevrilmiş Hali = %d"%ters)
 
