#include <stdio.h>
#include <stdlib.h>
int main() {

int i=1,n,toplam=0;
    
printf("Ust siniri giriniz: ");scanf("%d\n",&n);
for (i=1;i<n;i++){
toplam=i+toplam;
}
printf("Girilen sayinin ust siniri: %d\n",toplam);
return 0 ;
}
