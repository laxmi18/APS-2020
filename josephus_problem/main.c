#include <stdio.h>
#include <stdlib.h>
int josephus(int n, int k)
{
    int res=0;
    for(int i=1;i<=n;++i){
        res = (res+k)%i;
    }
    return res+1;
}
int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    printf("%d",josephus(n,k));
    return 0;
}
