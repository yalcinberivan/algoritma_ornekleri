x1=eval(input("Birinci kök: "))
x2=eval(input("İkinci kök: "))

ktop=x1+x2
kcarp=x1*x2

if (ktop<0):
    print("\nx^2+%0.3fx"%-1*ktop,end="")
else:
    print("\nx^2-%0.3fx"%ktop,end="")
if (kcarp<0):
    print("%0.3f"%kcarp)
else:
    print("+%0.3f"%kcarp)
