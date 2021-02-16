#include <stdio.h>
#include <conio.h>

int main()
{
    int n, i, t1, t2, t3;
    printf("Pozitif bir tamsayi giriniz: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        t1 += i;
    }

    for (i = 1; i <= n; i += 2)
    {
        t2 += i;
    }

    for (i = 2; i <= n; i += 2)
    {
        t3 += i;
    }

    printf("\n1'den %d'e kadar sayilarin toplami: %d\n", n, t1);
    printf("1'den %d'e kadar tek sayilarin toplami: %d\n", n, t2);
    printf("1'den %d'e kadar cift sayilarin toplami: %d\n", n, t3);

    return 0;
}