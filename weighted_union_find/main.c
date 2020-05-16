#include<stdio.h>
#define n 6

int arr[n];
int size[n];

void initialize()
{
    int i;
    for(i = 0; i<n; i++)
        arr[i] = i;
        size[i] = 1;
}

int root(int arr[],int i)
{
    while(arr[i] != i)
        i = arr[i];
    return i;
}

int Find(int *arr[],int a, int b)
{
    if(root(arr,a) == root(arr,b))
        return 1;
    else
        return 0;
}

int Union(int a ,int b)
{
    int root_a;
    int root_b;
    root_a = root(arr,a);
    root_b = root(arr,b);
    if(size[root_a] < size[root_b])
    {
        arr[root_a] = arr[root_b];
        size[root_b] += size[root_a];
    }
    else
    {
        arr[root_b] = arr[root_a];
        size[root_a] += size[root_b];
    }
}

int main()
{
    initialize();
    Union(0,1);
    Union(1,2);
    Union(3,2);
    //Union(1,4);

    int i;
    // output: 0 0 0 0 3 4 5
    for(i = 0; i <= n; i++)
        printf("%d\t", arr[i]);
    return 0;
}
