#include <stdio.h>

int main()
{
    int n = 7;
    int a[] = {31, 56, 78, 56, 91, 91, 31};
    int i;

    int temp = 0;
    for(i = 0; i < n ; i++)
        temp = temp ^ a[i];

    printf("Lonely element in array is %d\n", temp);
    return 0;
}
