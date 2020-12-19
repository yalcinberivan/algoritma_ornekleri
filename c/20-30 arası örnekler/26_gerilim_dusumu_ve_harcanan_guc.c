#include <stdio.h>
#include <math.h>

int main()
{
    int E, R1, R2, R3, R4, I, VR1, PR2;
    printf("Gerilimi giriniz: ");
    scanf("%d", &E);
    printf("Birinci direnci giriniz: ");
    scanf("%d", &R1);
    printf("Ikinci direnci giriniz: ");
    scanf("%d", &R2);
    printf("Ucuncu direnci giriniz: ");
    scanf("%d", &R3);
    printf("Dorduncu direnci giriniz: ");
    scanf("%d", &R4);
    I = E / (R1 + R2 + R3 + R4);
    VR1 = R1 * I;
    PR2 = pow(I, 2) * R2;
    printf("Devreden akan akim: %d\n", I);
    printf("R1 direncinde harcanan guc: %d\n", VR1);
    printf("R2 direncinde harcanan guc: %d\n", PR2);

    return 0;
}