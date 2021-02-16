#include <stdio.h>
#include <math.h>

int main()
{
    
#define PI 3.14
int r, aci, alan;

printf("Dairenin yaricapini giriniz: ");
scanf("%d", &r);
printf("Aradaki aciyi giriniz: ");
scanf("%d", &aci);
alan = (aci * PI * pow(r, 2)) / 360;
printf("Daire diliminin alani: %d\n", alan);

    return 0;
    }