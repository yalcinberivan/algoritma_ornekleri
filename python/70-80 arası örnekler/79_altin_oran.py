"""altın oran:herhangi bir AB doğru parçasının altın orana uygun olarak bölünmesi gerektiğinde
öyle bir C noktası bulunmalı ki CB/AC=AB/CB eşitliği sağlanmalıdır.
yani büyük parçanın,küçük parçaya oranı;tüm doğrunun,büyük parçaya oranına eşit olması gerekir."""

ab=int(input("AB doğru parçasının uzunluğunu bulunuz: "))
cb=2*ab/(1+5**0.5)
ac=ab-cb
print("AC uzunluğu:{:.2f}\n".format(ac) )
print("CB uzunluğu:{:.2f}\n".format(cb) )
