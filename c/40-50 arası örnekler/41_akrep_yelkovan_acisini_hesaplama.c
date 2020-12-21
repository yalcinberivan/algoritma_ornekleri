#include <stdio.h>
#include <math.h>
int main()
{
    int saat, ilerleme, dakika;
    printf("Saati giriniz: ");
    scanf("%d", &saat);
    printf("Dakikayi giriniz: ");
    scanf("%d", &dakika);
    ilerleme = dakika / 2;
    saat = 30 * saat;
    dakika = 6 * dakika;

    printf("Saat+ilerleme: %d\n", saat + ilerleme);
    printf("Dakika: %d\n", dakika);
    return 0;
}