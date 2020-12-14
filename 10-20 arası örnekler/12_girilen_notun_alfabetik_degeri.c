#include <stdio.h>
#include <stdlib.h>

int main(){

int note;
printf("Notunuzu giriniz: ");scanf("%d",&note);

if (note >= 90) 
printf("AA aldiniz");

else if (note >= 80) 
printf("BA aldiniz");

else if (note >=70 ) 
printf("BB aldiniz");

else if (note >= 65) 
printf("CC aldiniz");

else
printf("Dersten kaldiniz");

return 0;
    }
