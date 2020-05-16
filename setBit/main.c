#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    scanf("%d%d",&n,&i);
    int set = n | (1<<i);
    printf("%d",set);
    return 0;
}
