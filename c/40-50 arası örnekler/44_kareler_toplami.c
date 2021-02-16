#include <stdio.h>
#include <conio.h>

void main()
{
    int a, b, s;
    printf("Pozitif tamsayi: ");
    scanf("%u", &s);
    printf("\na-b\n");
    printf("=====\n");
    for (a = 0; a <= s; a++)
        for (b = 0; b <= s; b++)
            if (a * a + b * b == s)
                printf("%u-%u\n", a, b);

    getch();
}