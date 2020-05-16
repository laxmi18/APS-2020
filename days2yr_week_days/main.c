#include <stdio.h>
#include <stdlib.h>

int main()
{
    int days;
    int y,w,d;
    y = w = d = 0;
    scanf("%d",&days);
    y = days / 365;
    w = (days % 365) / 7;
    d = (days % 365) % 7;
    printf("Year:%d\nWeek:%d\nDays:%d\n",y,w,d);
    return 0;
}
