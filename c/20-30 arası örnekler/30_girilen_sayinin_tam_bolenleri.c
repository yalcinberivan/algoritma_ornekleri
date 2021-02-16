#include <stdio.h>
#include <conio.h>

int main()
{
    int sayi, i;
    printf("Pozitif tamsayi giriniz: ");
    scanf("%d", &sayi);
    printf("%d Tamsayisinin tam bolenleri:\n ", sayi);
    for (i = 1; i <= sayi; i++)
    {

        if (sayi % i == 0)
            printf("%d\n", i);
    }

    return 0;
}