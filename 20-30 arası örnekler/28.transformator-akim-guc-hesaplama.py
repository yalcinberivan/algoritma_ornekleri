vp=int(input("Tranfarmatörün primer gerilimi giriniz: "))
Ip=int(input("Tranfarmatörün akım gerilimi giriniz: "))
np=int(input("Tranfarmatörün sarım sayısı gerilimini giriniz: "))
ns=int(input("Tranfarmatörün seconder gerilimi giriniz: "))

vs=vp*ns/np
Is=Ip*np/ns
ps=vs*Is

if vs>vp :
    print("Yükseltici")
else:
    print("Düşürücü")