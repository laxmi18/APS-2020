#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c;
    scanf("%d %d",&a,&b);
    c = a;
    a = b;
    b = c;
    printf("a:%d\tb:%d\n",a,b);
    return 0;
}
