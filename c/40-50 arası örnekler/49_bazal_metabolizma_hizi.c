#include <stdio.h>

int main()
{
    int k, b, y, bmh;
    char c;
    printf("Kilonuzu giriniz: ");
    scanf("%d", &k);
    printf("Boyunuzu giriniz: ");
    scanf("%d", &b);
    printf("Yasinizi giriniz: ");
    scanf("%d", &y);
    printf("Cinsiyetizi giriniz: ");
    scanf("%s", &c);

    if (c == 'E' || c == 'e')
    {
        bmh = (66.473 + 13.7516 * k + 5.0033 * b - 6.775 * y);
    }
    else
        bmh = (665.0955 + 9.5634 * k + 1.8496 * b - 4.6756 * y);
    printf("Bazal metabolizma hizi: %d\n", bmh);

    return 0;
}