#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, product = 0,i;
    scanf("%d %d",&a,&b);
    for(i=1;i<=b;i++){
        product = product + a;
    }
    printf("%d\n",product);
    return 0;
}
