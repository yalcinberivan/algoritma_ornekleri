#include <stdio.h>
#include <math.h>

int main()
{

#define PI 3.14
    int a, b, d, aci;
    double derece, c, sonuccos;

    printf("Birinci kenari giriniz:");
    scanf("%d", &a);
    printf("Ikinci kenari giriniz: ");
    scanf("%d", &b);
    printf("Aradaki aciyi giriniz: ");
    scanf("%d", &aci);
    printf("Dereceyi giriniz: ");
    scanf("%lf", &derece);

    sonuccos = cos(derece);

    c = pow(a, 2) + pow(b, 2) - 2 * a * b * cos(aci * PI / 180);
    d = pow(c, 0.5);

    printf("Sonuc: %d\n", d);

    return 0;
}
