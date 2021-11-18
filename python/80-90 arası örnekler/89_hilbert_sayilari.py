"""Hilbert sayısı:1,5,9,13,9,17,21,25,29,33 gibi 4k+1 şeklinde ifade edilebilen pozitif tamsayılar,
"hilbert sayısı olarak adlandırılır.klavyeden girilne pozitif bir tamsayının hilbert sayısı olup olmadığını 
test eden program. """

sayi=int(input("Tamsayı giriniz:  "))
if((sayi-1)%4==0):
    print("Hilbert sayısıdır...")
else:
    print("Hilbert sayısı değildir...")
    