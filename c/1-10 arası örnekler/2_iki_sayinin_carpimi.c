#include<stdio.h>

int sayi1,sayi2,carpim;
main()
{
	printf("Birinci sayiyi giriniz: ");scanf("%d",&sayi1);
    printf("Ikinci sayiyi giriniz: ");scanf("%d",&sayi2);

    carpim = sayi1 * sayi2;

    printf("Sayilarin carpimi: %d\n",carpim);
}