#include <stdio.h>
#include <conio.h>
int main()
{
    int a, b, sec;
    printf("Uzunlugu giriniz: ");
    scanf("%d", &a);
    printf("\nDonusturme\n1-mm\n2-cm\n3-dm\n4-km\n");
    printf("\nSeciminiz: ");
    scanf("%d", &sec);
    switch (sec)
    {
    case 1:
    {
        b = 1000 * a;
        break;
    }
    case 2:
    {
        b = 100 * a;
        break;
    }
    case 3:
    {
        b = 10 * a;
        break;
    }
    case 4:
    {
        b = a / 1000;
        break;
    }

    default:
        b = 0;
    }
    printf("Sonuc: %d\n", b);
    return 0;
}