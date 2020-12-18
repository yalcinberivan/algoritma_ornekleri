#include <stdio.h>
#include <math.h>
int main(){   

int a,b,c,d;

printf("Birinci dik kenari giriniz: ");scanf("%d",&a);
printf("Ikinci dik kenari giriniz: ");scanf("%d",&b);

c=pow(a,2)+pow(b,2);

d=pow(c,0.5);

printf("Sonuc:%d\n",d);

    return 0;
} 