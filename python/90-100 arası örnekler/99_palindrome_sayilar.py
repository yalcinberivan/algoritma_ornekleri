"""Palindrome sayı: baştan ve sondan yazılışları/okunuşları aynı olan tamsayılara denir."""

#3 basamaklı palindrome sayıları için:
print("### Üç basamaklı palindrome sayılar ###")
for i in range (1,9):
    for j in range (1,9):
        print(100*i+10*j+i)
print("\n********************************\n********************************\n")
        
# 4 basamaklı palindrome sayıları için:
print("### Dört basamaklı palindrome sayılar ###")
for k in range (1,9):
    for z in range (1,9):
        print(1000*k+100*z+10*z+k)
