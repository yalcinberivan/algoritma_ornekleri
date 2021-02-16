#include <stdio.h>
#include <conio.h>

main()
{
    float x, y;
    printf("X noktasini giriniz: ");
    scanf("%f", &x);
    if (x < 0)
        y = 1;
    else if ((0 < x) && (x <= 2))
        y = x;
    else if ((2 < x) && (x <= 4))
        y = 3;
    else
        y = 4 - x;
    printf("Fonksiyonun x=%0.2f noktasindaki degeri=%0.2f", x, y);
    getch();

    return 0;
}