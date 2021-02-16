#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sayi;
    printf("Lutfen bir sayi giriniz: ");
    scanf("%d", &sayi);
    if (sayi % 2 == 0)
        printf("Girilen sayi cifttir");
    else
        printf("Girilen sayi negatiftir");

    return 0;
}