#include <stdio.h>
#include <math.h>

int main()
{
#define PI 3.14
    int v, i, fi, s, gf, p, q;
    printf("Akimin volt cinsinden faz acisini giriniz: ");
    scanf("%d", &v);
    printf("Akimin amper cinsinden faz acisini giriniz: ");
    scanf("%d", &i);
    printf("Akimin derece cinsinden faz acisini giriniz: ");
    scanf("%d", &fi);
    fi = fi * PI / 180;
    s = v * i;
    gf = cos(fi);
    p = s * gf;
    q = s * sin(fi);
    printf("Akimin aktif gucu: %d\n", p);
    printf("Akimin reaktif gucu: %d\n", q);
    printf("Akimin gorunur gucu: %d\n", s);
    printf("Akimin guc faktoru: %d\n", gf);
    return 0;
}