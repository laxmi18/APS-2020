#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, count=0;
    scanf("%d",&n);
    while (n!=0)
    {
        n=n&(n-1);
        count++;
    }
    printf("%d",count);
    return 0;
}
