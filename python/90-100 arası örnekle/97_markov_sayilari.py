"""Markov sayısı:x**2+y**2+z**2=3xyz markov denkleminin pozitif tamsayı olan x,y,z şeklindeki çözümleridir
ör:(1,1,1),(1,1,2),(1,2,5),(1,5,13) vb. çözüm için üç tane döngü açılarak,döngü değerlerinin markov denklemini
sağlayıp sağlayamadıkları kontrol edilir.programın aynı sayıların farklı kombinasyonlarını listelememesi için iç döngüler,
dış döngülerden başlatılır.Böylece (1,1,2),(1,2,1),(2,1,1) kombinasyonlarından sadece (1,1,2) listelenmektedir."""

for x in range (1,50,1):
    for y in range (x,50,1):
        for z in range (y,50,1):
            if(x*x+y*y+z*z==3*x*y*z):
                print("(",x,y,z,")")
                