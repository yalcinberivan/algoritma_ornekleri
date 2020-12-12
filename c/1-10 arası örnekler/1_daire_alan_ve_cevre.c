#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int r,alan,cevre,pi=3;
main()
{
	printf("Lutfen Yaricapi giriniz: ");scanf("%d",&r);

    alan=pi*r*r;
    cevre=2*pi*r;

    printf("Cemberin yaricapi: %d\n",r);
    printf("Cemberin alani: %d\n",alan);
    printf("Cemberin cevresi: %d ",cevre);
}
