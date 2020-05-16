#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void bottomUpHeap(int n, int H[])
{
    int k,v,j;
    int heap;
    for(int i=(floor(n/2));i>=1;i--){
        k=i;
        v=H[i];
        heap = 0;
        while((!heap) && ((2*k)<=n)){
            j=2*k;
            if (j<n)
                if (H[j]<H[j+1])
                j=j+1;
            if (v>=H[j])
                heap = 1;
            else{
                H[k]=H[j];
                k=j;
            }
        }
        H[k]=v;
    }
}
int main()
{
    int n=7;
    int H[] = {0,2,9,7,6,5,8};
    bottomUpHeap(n,H);
    for(int i=0;i<n;i++)
    printf("%d\n",H[i]);
    return 0;
}
