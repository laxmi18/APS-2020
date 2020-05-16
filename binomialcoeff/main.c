#include <stdio.h>
#include <stdlib.h>
int min(int a, int b)
{
    if(a<b)
        return a;
    else
        return b;
}
int main()
{
    int i,j,n,k,c[1000][1000];
    scanf("%d%d",&n,&k);
    for(i=0;i<=n;i++){
        for(j=0;j<=min(i,k);j++){
            if ((j=0) || (i==j))
                c[i][j] = 1;
            else
                c[i][j] = c[i-1][j-1] + c[i-1][j];
        }
    }
    printf("%d",c[n][k]);
    return 0;
}
