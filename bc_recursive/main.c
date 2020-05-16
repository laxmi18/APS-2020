#include <stdio.h>
#include <stdlib.h>

int bc(int n,int k)
{
    if((n==k)|| (k=0))
        return 1;
    else
        return(bc(n-1,k-1) + bc(n-1,k));
}
int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    int result = bc(n,k);
    printf("%d",result);
    return 0;
}
