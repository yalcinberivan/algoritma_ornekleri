#include <stdio.h>

int main()
{

    int i = 0;
    for (i = 0; i <= 10; i++)
    {
        printf("%d--", i);
    }

    printf("\n");

    int j = 0;
    for (j = 1; j < 10; j++)
    {
        printf("%d--", j);
    }

    printf("\n");

    int k = 0;
    for (k = 1; k <= 10; k += 2)
    {
        printf("%d--", k);
    }

    printf("\n");

    int l = 0;
    for (l = 0; l <= 10; l += 2)
    {
        printf("%d--", l);
    }

    return 0;
}