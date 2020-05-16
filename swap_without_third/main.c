#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b;
    scanf("%d %d",&a,&b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("a:%d\tb:%d",a,b);
    return 0;
}
