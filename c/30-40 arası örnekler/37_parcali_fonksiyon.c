#include <stdio.h>
#include <conio.h>
int main()
{
    int x, y;
    printf("x noktasini giriniz: ");
    scanf("%d", &x);
    if (x < 0)
        y = 1;
    else if ((0 <= x) && (x <= 2))
        y = x;
    else if ((2 <= x) && (x <= 4))
        y = 3;
    else
        y = 4 - x;
    printf("Fonksiyonun %d noktasidaki degeri: %d\n", x, y);

    return 0;
}