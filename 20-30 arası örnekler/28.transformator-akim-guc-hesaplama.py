vp=int(input("Tranformatörün primer gerilimi giriniz: "))
Ip=int(input("Tranformatörün akım gerilimi giriniz: "))
np=int(input("Tranformatörün sarım sayısı gerilimini giriniz: "))
ns=int(input("Tranformatörün seconder gerilimi giriniz: "))

vs=vp*ns/np
Is=Ip*np/ns
ps=vs*Is

if vs>vp :
    print("Yükseltici")
else:
    print("Düşürücü")
