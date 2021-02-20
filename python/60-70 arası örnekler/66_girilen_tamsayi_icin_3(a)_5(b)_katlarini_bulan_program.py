# 7 den büyük tamsayılar (s>7),3 ve 5 in katlarının toplamı (3a+5b=s) olarak yazılabilir.
# Girilen tamsayı için 3 (a) ve 5(b) in katlarını bulan program.

s=int(input("7'den büyük bir tamsayıyı giriniz: "))
for a in range(int(s/3)):
    for b in range(int(s/5)):
        if (3*a+5*b==s):
            print(a)
            print(b)
            break
else:
    print("Geçerli bir sayı giriniz...")           