#include <stdio.h>
#include <math.h>

int main()
{
    int h, vo, t, t1, x, vy, v, v1;
    printf("Yerden yuksekligi giriniz: ");
    scanf("%d", &h);
    printf("Hizi giriniz: ");
    scanf("%d", &vo);
    t = 2 * h / 9.8;
    t1 = pow(t, 0.5);
    x = vo * t1;
    vy = 9.8 * t1;
    v = pow(vo, 2) + pow(vy, 2);
    v1 = pow(v, 0.5);
    printf("Gecen sure: %d\n", t1);
    printf("Cismin hizi: %d\n", x);
    printf("Cismin t sure sonraki hizi: %d\n", v1);

    return 0;
}