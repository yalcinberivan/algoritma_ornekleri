#include <stdio.h>
#include <math.h>

int main()
{
    int m, v, h, ep, ek;
    printf("Maddenin kutlesini giriniz: ");
    scanf("%d", &m);
    printf("Maddenin yerden yuksekligini giriniz: ");
    scanf("%d", &v);
    printf("Maddenin hizini giriniz: ");
    scanf("%d", &h);

    ep = m * 9.8 * h;
    ek = (m * pow(v, 2)) / 2;

    printf("Maddenin potansiyel enerjisi: %d\n", ep);
    printf("Maddenin kinetik enerjisi: %d\n", ek);

    return 0;
}