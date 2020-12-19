#include <stdio.h>
#include <math.h>

int main()
{
    int mo, dt, t, n, m ;
    printf("Baslangic kutlesini giriniz: ");
    scanf("%d", &mo);
    printf("Yarilanma suresini giriniz: ");
    scanf("%d", &dt);
    printf("Sureyi giriniz: ");
    scanf("%d", t);
    n = t / dt;
    m = mo / pow(2, n);
    printf("Yarilanma suresi: %d\n", dt);
    printf("Kalan kutle: %d/n", m);

    return 0;
}