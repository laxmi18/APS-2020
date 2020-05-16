#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;
    scanf("%d",&n);
    int noOfdigits = floor(log10(n)+1);
    printf("%d",noOfdigits);
    return 0;
}
