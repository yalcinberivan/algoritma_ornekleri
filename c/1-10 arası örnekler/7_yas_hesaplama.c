#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{

    int dt, yas;

    printf("Lutfen dogum tarihinizi giriniz: ");
    scanf("%d", &dt);

    time_t seconds = time(NULL);
    struct tm *current_time = localtime(&seconds);
    int simdikiYil = current_time->tm_year + 1900;

    yas = simdikiYil - dt;

    printf("Dogum tarihiniz: %d\n", yas);

    return 0;
}