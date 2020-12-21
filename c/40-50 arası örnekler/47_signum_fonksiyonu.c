#include <stdio.h>

int main()
{
    int fx, x;
    printf("X degerini giriniz: ");
    scanf("%d", &x);
    fx = x * x - 5 * x + 3;
    if (fx < 0)
        printf("-1");
    else if (fx = 0)
        printf("0");
    else
        printf("1");

    return 0;
}