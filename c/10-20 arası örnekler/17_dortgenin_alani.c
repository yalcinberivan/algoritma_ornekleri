#include <stdio.h>
#include <math.h>

int main()
{

#define PI 3.14
    int a, b, aci, alan, derece, sonucsin;

    printf("Birinci kosegeni giriniz: ");
    scanf("%d", &a);
    printf("Ikinci kosegeni  giriniz: ");
    scanf("%d", &b);
    printf("Aradaki aciyi giriniz: ");
    scanf("%d", &aci);
    printf("Dereceyi giriniz: ");
    scanf("%d", &derece);

    sonucsin = sin(derece);
    alan = a * b * sin(aci * PI / 180) / 2;
    printf("Dortgenin alani: %d\n", alan);

    return 0;
}