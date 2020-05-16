#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    scanf("%d %d:",&n,&i);
    if(n & (1<<i))
        printf("set");
    else
        printf("not set");
    return 0;
}
