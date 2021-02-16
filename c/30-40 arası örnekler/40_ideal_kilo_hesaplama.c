#include <stdio.h>
#include <conio.h>
int main()
{
    int b, ik, c;
    printf("Boyunuzu giriniz: ");
    scanf("%d", &b);
    printf("Cinsiyetiniz [1-Erkek / 2-Kadin]: ");
    scanf("%d", &c);
    if (c == 1)
        ik = 50 + 2.3 * (b / 2.54 - 60);
    else
        ik = 45.5 + 2.3 * (b / 2.54 - 60);
    printf("\nIdeal kilonuz (kg): %d\n", ik);

    return 0;
}