#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num[10000];
    int i, n, j, k, temp;
    printf("Enter n: ");
    scanf("%d",&n);
    printf("\nEnter n numbers:\n");
    for (i=0;i<n;i++)
    {
        scanf("%d",&num[i]);
    }
    for(j=1;j<=n;j++){
        for(i=0;i<n-1;i++){
            temp = num[i];
            num[i] = num[i+1];
            num[i+1] = temp;
            for(k=0;k<n;k++)
                printf("%d",num[k]);
            printf("\n");
        }
    }
    return 0;
}
