#include <stdio.h>
#include <conio.h>
#include <math.h>

float a, b, c, d, x1, x2;
main()
{
    printf("Ax^2+Bx+C=0\n");
    printf("A= ");
    scanf("%f", &a);
    printf("B= ");
    scanf("%f", &b);
    printf("C= ");
    scanf("%f", &c);
    printf("\n");
    d = b * b - 4 * a * c;
    if (d > 0)
    {

        printf("Gercel kokler vardir:\n");
        x1 = (-b - sqrt(d)) / (2 * a);
        x2 = (-b + sqrt(d)) / (2 * a);
        printf("Kokler: %0.2f\t%0.2f", x1, x2);
    }

    else if (d == 0)
    {
        printf("Katli kok vardir:\n");
        x1 = -b / (2 * a);
        printf("Katli kok: %0.2f", x1);
    }
    else
        printf("Sanal kokler vardir.");

    getch();
        return 0;
}
