#include <stdio.h>
#include <conio.h>
void main()
{
    float s;
    printf("Bir sayi giriniz: ");
    scanf("%f", &s);
    if (s == (int)s)
        printf("Tamsayi");
    else
        printf("Tamsayi degil");

    return 0;
}