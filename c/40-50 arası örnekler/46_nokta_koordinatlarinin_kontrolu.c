#include <stdio.h>

int main()
{
    int x1, y1, x2, y2, x3, y3;
    printf("X1 noktasini giriniz: ");
    scanf("%d", &x1);
    printf("Y1 noktasini giriniz: ");
    scanf("%d", &y1);
    printf("X2 noktasini giriniz: ");
    scanf("%d", &x2);
    printf("Y2 noktasini giriniz: ");
    scanf("%d", &y2);
    printf("X3 noktasini giriniz: ");
    scanf("%d", &x3);
    printf("Y3 noktasini giriniz: ");
    scanf("%d", &y3);

    if ((x3 > x1) && (y3 > y1) && (x3 < x2) && (y3 < y2))
        printf("Icinde");
    else
        printf("Icinde degil");

    return 0;
}