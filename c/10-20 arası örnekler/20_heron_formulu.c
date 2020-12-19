#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, c, u, alan, alan2;
    printf("Birinci kenari giriniz: ");
    scanf("%d", &a);
    printf("Ikinci kenari giriniz: ");
    scanf("%d", &b);
    printf("Ucuncu kenari giriniz: ");
    scanf("%d", &c);
    u = (a + b + c) / 2;
    alan = (u * (u - a) * (u - b) * (u - c));
    alan2 = pow(alan,0.5);
    printf("Sonuc: %d\n", alan2);
    return 0;
}