#include <stdio.h>
#include <stdlib.h>

int max(int a, int b, int c)
{
    if(a > b && a > c)
        return a;
    else if(b > a && b > c)
        return b;
    else if(c > a && c > b)
        return c;
}

void rodCuttingMaxProduct(int n, int arr[])
{
    int a[50], i, j;
    a[0] = 0;
    a[1] = 0;
    for(i=2; i<=n; i++)
    {
        a[i] = 0;
        for(j=1; j<=(i/2); j++)
        {
            a[i] = max(a[i] , j*(i-j), j*a[i-j]);
        }
    }
    for(i=0;i<=n;i++)
    {
        printf("%d\n",a[i]);
    }
}

int main()
{
    int n,i,price[500];
    printf("Enter length!\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%d",&price[i]);
    }
    rodCuttingMaxProduct(n,price);
    return 0;
}
