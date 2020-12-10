b=eval(input("Boyunuzu giriniz: "))

c=int(input("Cinsiyetiniz [1-erkek / 2-kadın]: "))

if (c==1):
    ik=50+2.3*(b/2.54-60)
else:
    ik=45+2.3*(b/2.54-60)
print("\nİdeal kilonuz (kg): %0.2f"%ik)
