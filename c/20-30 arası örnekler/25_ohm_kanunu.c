#include <stdio.h>
#include <math.h>

int main()
{
    int R, I, V;
    printf("Iletkenin direncini giriniz: ");
    scanf("%d", &R);
    printf("Iletkenin icinden akam akimi giriniz: ");
    scanf("%d", &I);
    V = R * I;
    printf("Iletkenin uclarindaki gerilim:%d\n", V);
    return 0;
}