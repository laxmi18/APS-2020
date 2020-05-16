#include <stdio.h>
#include <stdlib.h>

int main()
{
    int year;
    scanf("%d",&year);
    if((year % 4 == 0 || year % 400 == 0) && (year % 100 != 0)){
        printf("Leap Year\n");
    }
    else
        printf("Not a leap year\n");
    return 0;
}
