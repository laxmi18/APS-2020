#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    scanf("%d%d",&n,&i);
    int unset = n & -(1<<i);
    printf("%d",unset);
    return 0;
}
