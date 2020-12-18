#include <stdio.h>
#include <conio.h>
#include <math.h>

int main()
{

    int a, b, aci, alan;
    printf("Birinci kenari giriniz: ");
    scanf("%d", &a);
    printf("Ikinci kenari giriniz: ");
    scanf("%d", &b);
    printf("Aradaki aciyi giriniz: ");
    scanf("%d", &aci);

    alan = a * b * sin(M_PI * aci / 180) / 2;

    printf("Ucgenin alani: %d\n", alan);

    return 0;
}