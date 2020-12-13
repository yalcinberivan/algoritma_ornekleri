#include<stdio.h>
#include<conio.h>

void main(){
    int i,N; float t=0;
    clrscr();
    printf("Tek sayilarin ust siniri: ");scanf("%u",&N); 
    i=1;

while(i<=N)  do{t+=i ; i+=2;}

printf("\ntoplami:%0.0f",t);
getch();

}