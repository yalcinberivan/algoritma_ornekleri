#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m, ma, mol;
    printf("Maddenin kutlesini giriniz: ");
    scanf("%d", &m);
    printf("Maddenin molekul agirligini giriniz: ");
    scanf("%d", &ma);
    mol = m / ma;
    printf("Mol sayisi: %d\n ", mol);
    return 0;
}