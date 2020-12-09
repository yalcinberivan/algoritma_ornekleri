import datetime


dogumyili=int(input("Doğum yılınızı giriniz: "))

now = datetime.datetime.now()

yas=now.year-dogumyili

print("yaşınız: ",yas)


