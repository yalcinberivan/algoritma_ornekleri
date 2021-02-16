#include <stdio.h>
#include <stdlib.h>

int main()
{
int vp, ip, np, ns, vs, is, ps;

printf("Transformatorun primer gerilimini giriniz: ");
scanf("%d", &vp);
printf("Transformatorun akim gerilimini giriniz: ");
scanf("%d", &ip);
printf("Tranformatorun sarim sayisi gerilimini giriniz: ");
scanf("%d", &np);
printf("Tranformatorun seconder gerilimi giriniz: ");
scanf("%d", &ns);

vs = vp * ns / np;
is = ip * np / ns;
ps = vs * is;

if (vs > vp)

    printf("Yukseltici tranfarmator");
else
    printf("Dusurucu transfarmator");

    return 0;
    }