#include <stdio.h>
#include <stdlib.h>

int main()
{

    int i = 1, faktoriyel = 1, sayi = 0;

    printf("Lutfen faktoriyelini hesaplamak istediginiz sayiyi giriniz:");
    scanf("%d", &sayi);

    for (i = 1; i <= sayi; i++)
    {
        faktoriyel = faktoriyel * i;
    }

    printf("Sayinin faktoriyeli %d\n", faktoriyel);

    return 0;
}
