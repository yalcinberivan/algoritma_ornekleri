#include <stdio.h>
#include <conio.h>

int main(){

int a; 
printf("Bir tamsayi giriniz: "); scanf("%d",&a);

if (a>0) printf("Pozitif");

else if (a<0) printf("Negatif");

else printf("Sifir");



    return 0 ;
}