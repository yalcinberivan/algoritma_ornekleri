#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, c, x;
    printf("ax+b=c\n");
    printf("a katsayisi: ");
    scanf("%d", &a);
    printf("b katsayisi: ");
    scanf("%d", &b);
    printf("c katsayisi: ");
    scanf("%d", &c);
    x = (c - b) / a;
    printf("\nDenklemin koku: %d\n", x);

    return 0;
}