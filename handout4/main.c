#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[] = {'a','b','c'};
    int n=3;
    for(int i=0;i<(1<<n);i++){
        for(int j=0;j<n;j++){
            if(i&(1<<j))
                printf("%c",a[j]);
            printf("\n");
        }
    }
    return 0;
}
