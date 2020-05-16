#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    printf("A-Z\n");
    for(i=65;i<91;i++){
        printf("%c\t",i);
    }
    printf("\na-z\n");
    for(i=97;i<123;i++){
        printf("%c\t",i);
    }
    return 0;
}
