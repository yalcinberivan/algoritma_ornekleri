#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, n, r, f1 = 1, f2 = 1, f3 = 1, k;
    printf("n= ");
    scanf("%d", &n);
    printf("r= ");
    scanf("%d", &r);
    for (i = 1; i <= n; i++)
    {
        f1 *= i;
        if (i <= r)
            f2 *= i;
        if (i <= n - r)
            f3 *= i;
    };

    k = f1 / (f2 * f3);
    printf("Sonuc: %d\n", k);

    return 0;
}