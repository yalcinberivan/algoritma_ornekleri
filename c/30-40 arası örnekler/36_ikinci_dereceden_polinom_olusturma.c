#include <stdio.h>
#include <conio.h>

void main()
{
    float x1, x2, ktop, kcarp;
    printf("1.kok: ");
    scanf("%f", &x1);
    printf("2.kok: ");
    scanf("%f", &x2);
    ktop = x1 + x2;
    kcarp = x1 * x2;
    if (ktop < 0)
        printf("\nx^2+%0.3f", -1 * ktop);
    else
        printf("\nx^2-%0.3fx", ktop);

    if (kcarp < 0)
        printf("%0.3f", kcarp);
    else
        printf("+%0.3f", kcarp);

    getch();
}