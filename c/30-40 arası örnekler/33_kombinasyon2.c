#include <stdio.h>
#include <conio.h>

float faktoriyel(int x)
{
    int y;
    float z = 1;
    for (y = 1; y <= x; y++)
        z *= y;
    return z;
}
void main()
{
    int n, r;
    float f1, f2, f3, k;
    printf("Kombinasyon(n-r)\n\n");
    printf("n= ");
    scanf("%u", &n);
    printf("r= ");
    scanf("%u", &r);
    f1 = faktoriyel(n);
    f2 = faktoriyel(r);
    f3 = faktoriyel(n - r);
    k = f1 / (f2 * f3);
    printf("\nKombinasyon(%d,%d)=%0.0f", n, r, k);

    getch();
}
