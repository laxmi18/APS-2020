#include <stdio.h>
#include <stdlib.h>

int subsetsum(int a[][], int n, int sum, int ss[])
{
    int i,j;
    for(i=0;i<=sum;i++){
        a[0][i]=0;
    }
    for(i=0;i<=n;i++){
        a[i][0]=1;
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=sum;j++){
            if(a[i-1][j] == 1)
                a[i][j]=1;
            if(j<ss[i-1])
            a[i][j]=0;
            else
                a[i][j]=a[i-1][j-ss[i-1]];
        }
    }
    return (a[n][sum]);
}
int main()
{
    int n=5;
    int ss[]={1,2,3,5,7};
    int sum=9;
    int a[1000][1000];
    int result = subsetsum(a,n,sum,ss);
    printf("%d",result);
    return 0;
}
