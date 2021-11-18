#include <stdio.h>
#include <math.h>

int main()
{

int a, b, c, x1, y1, uz, uz1;

printf("X'in katsayisini giriniz: ");
scanf("%d", &a);
printf("Y'nin katsayisini giriniz: ");
scanf("%d", &b);
printf("Sabiti giriniz: ");
scanf("%d", &c);
printf("X1 noktasini giriniz: ");
scanf("%d", &x1);
printf("Y1 noktasini giriniz: ");
scanf("%d", &y1);

if (a * x1 + b * y1 + c == 0)
    printf("Girilen nokta dogrunun uzerindedir.");
else
    uz = abs(a * x1 + b * y1 + c) / pow((a * a + b * b), 0.5);
    printf("Girilen nokta,dogru uzerinde degildir.Noktanin dogruya uzakligi %d birimdir.", uz);
    return 0;
    }