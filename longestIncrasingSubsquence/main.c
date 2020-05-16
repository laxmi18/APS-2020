#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[10000], n, i, j, LIS[100000];
    scanf("%d",&n);
    for(i=0;i<=n;i++){
        scanf("%d",&a[i]);
        LIS[i] = 1;
    }
    for (i=1;i<=n;i++){
        for(j=0;j<=i;j++){
            if((a[i]>a[j]) && (LIS[j]+1>LIS[i]))
                LIS[i] = LIS[j]+1;
        }
    }
    for(i=0;i<=n;i++)
    printf("%d\t",LIS[i]);
    return 0;
}
