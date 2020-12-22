#include <stdio.h>
#include <math.h>
int main()
{
    int b, y, bki, k, yontem;
    char c;
    printf("Yontemi giriniz (1,2,3,4): ");
    scanf("%d", &yontem);

    if (yontem == 1)
    {
        printf("Boyunuzu giriniz: ");
        scanf("%d", &b);
        printf("Cinsiyetinizi giriniz : ");
        scanf("%s", &c);
        if ((c == 'E') || (c == 'e'))
            bki = 50.5 + 2.3 * (b - 60);
        else
            bki = 45.5 + 2.3 * (b - 60);
        printf("Ideal vucut agirligi : %d\n", bki);
    }

    if (yontem == 2)
    {
        printf("Boyunuzu giriniz: ");
        scanf("%d", &b);
        printf("Yasinizi giriniz: ");
        scanf("%d", &y);
        printf("Cinsiyetinizi giriniz : ");
        scanf("%s", &c);
        if ((c == 'E') || (c == 'e'))
            bki = (b - 100 + y / 10) * 0.9;
        else
            bki = (b - 100 + y / 10) * 0.8;
        printf("Ideal vucut agirligi : %d\n", bki);
    }

    if (yontem == 3)
    {
        printf("Boyunuzu giriniz: ");
        scanf("%d", &b);
        printf("Kilonuzu giriniz: ");
        scanf("%d", &k);
        bki = k / (b * b);
        if (bki <= 17.5)
            printf("Anoreksi,asiri zayif,yuksek risk");
        else if ((bki > 17.5) && (bki < 20.7))
            printf("Zayif");
        else if ((bki >= 20.7) && (bki < 26.4))
            printf("Normal kilolu");
        else if ((bki >= 26.4) && (bki < 27.8))
            printf("Biraz fazla kilolu");
        else if ((bki >= 27.8) && (bki < 31.1))
            printf("Fazla kilolu");
        else if ((bki >= 31.1) && (bki < 34.9))
            printf("Cok fazla kilolu");
        else if ((bki >= 35) && (bki < 40))
            printf("Saglık acisindan yuksek riskli kilolu");
        else if ((bki >= 40) && (bki < 50))
            printf("Hastalikli bir sekilde kilolu");
        else
            printf("Süper asiri kilolu");
    }

    if (yontem == 4)
    {
        printf("Boyunuzu giriniz: ");
        scanf("%d", &b);
        printf("Kilonuzu giriniz:\n ");
        scanf("%d", &k);
        bki = k / (b * b);
        if (bki < 18.5)
            printf("Zayif");
        else if ((bki >= 18.5) && (bki < 25))
            printf("Orta");
        else if ((bki >= 25) && (bki < 30))
            printf("Fazla kilolu");
        else if ((bki >= 30) && (bki < 35))
            printf("1.derece obez");
        else if ((bki >= 35) && (bki < 40))
            printf("2.derece obez");
        else
            printf("3.derece morbid obez");
    }
    return 0;
}