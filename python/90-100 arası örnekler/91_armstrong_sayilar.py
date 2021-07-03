"""Armstrong sayı:herbir hanenin basamak sayısı kadar üslerinin toplamı yine aynı sayıya eşit olan tamsayılara
"armstrong sayı" denir. (ör:153=1**3+5**3+3**3) """
#100-999 arasındaki armstrong sayıları listeleyen program

for i in range(1,9):
    for j in range(0,9):
        for k in range(0,9):
            s=100*i+10*j+k
            if(s==i**3+j**3+k**3):
                print(s)
    