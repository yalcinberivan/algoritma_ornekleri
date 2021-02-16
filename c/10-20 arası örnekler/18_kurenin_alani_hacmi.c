#include <stdio.h>
#include <math.h>

int main()
{

#define PI 3.14
int r, alan, hacim;

printf("Yaricapi giriniz: ");
scanf("%d",&r);

alan = 4 * PI * pow(r, 2);
hacim=(4*PI*pow(r,3))/3;

printf("Kurenin hacmi: %d\n",hacim);
printf("Kurenin alani: %d\n",alan);


    return 0;
    }
