#include <stdio.h>
#include <stdlib.h>

int BIT[1000], a[1000], n=10;
void update(int index, int value)
{
    for(;index<=n;index+=(index&-index)){
            BIT[index] += value;
    }
}
int query(int i)
{
    int querysum = 0;
    for(;i>0;i=i-(i&-i)){
        querysum += BIT[i];
    }
    return querysum;
}
int main()
{
    int i, value;
    a[10] = {1,2,3,4,5,6,7,8,9,10};
    while(i<=n){
        scanf("%d %d",&i,&value);
        update(i,value);
    }
    query(5);
    return 0;
}
