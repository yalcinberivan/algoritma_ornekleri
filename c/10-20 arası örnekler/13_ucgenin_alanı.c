#include <stdio.h>
#include <conio.h>

int main()
{

    int a, h, alan;

    printf("Kenar uzunlugunu giriniz: ");
    scanf("%d", &a);
    printf("Yuksekligi giriniz: ");
    scanf("%d", &h);

    alan = a * h / 2;

    printf("Ucgenin alani: %d\n", alan);

    return 0;
}