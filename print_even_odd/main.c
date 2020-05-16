#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i;
    scanf("%d",&n);
    int even[100],odd[100];
    printf("EVEN\tODD\n");
    for(i=1;i<=n;i++){
        if(i%2==0){
            printf("%d\t",i);
        }
        else{
            printf("%d\n",i);
        }
    }
    return 0;
}
