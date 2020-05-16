#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int q, n, b, i;
    scanf("%d",&q);
    for(i=0;i<q;i++){
        scanf("%d %d",&n,&b);
        if(b==2)
            printf("%d",floor(log10(n)+1));
    }
    printf("%d",log10(100));
}
