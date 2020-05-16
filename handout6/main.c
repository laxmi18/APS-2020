#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void find(int a[], int l, int s)
{
    for(int i=1;i<(pow(2,l));i++){
        int sum=0;
        for(int j=0;j<l;j++){
            if((i>>j)&1)
                sum += a[j];
        }
            if(sum==s){
                printf("yes\n");
                return;
            }
    }
    printf("no\n");
}
int main()
{
    int sum = 5, n=4;
    int a[] = {-1,2,4,121};
    find(a,n,sum);
    return 0;
}
