h=int(input("Uzunluğu (h) giriniz: "))
for a in range(h):
    for b in range(h):
        c=(a**2+b**2)**(1/2)
        if (c<h) and (c==int(c)):
            print("Evet")
            print(a)
            print(b)
            print(c)
            break
    else:
        print("Hayır")
        