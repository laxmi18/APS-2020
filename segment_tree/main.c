#include<stdio.h>

int tree[400005]={0};

int min(int a,int b){
    return a>b?b:a;
}

void build(int v,int s,int e,int arr[]){
    if(s == e){
        tree[v]=arr[s];
        return;
    }

    int m=(s+e)/2;
    build(2*v,s,m,arr);
    build(2*v+1,m+1,e,arr);

    tree[v] = min(tree[2*v],tree[2*v+1]);
}

void update(int v,int s,int e,int p,int val,int arr[]){
    if(s == e){
        tree[v] = val;
        arr[s] = val;
        return;
    }

    int m=(s+e)/2;

    if(p<=m) update(2*v,s,m,p,val,arr);
    else update(2*v+1,m+1,e,p,val,arr);

    tree[v] = min(tree[2*v],tree[2*v+1]);
}

int query(int v,int s,int e,int l,int r){
    if(s > r || e < l) return 100005;

    if(s >= l && r >= e) return tree[v];

    int m = (s+e)/2;

    int l_a = query(2*v,s,m,l,r);
    int r_a = query(2*v+1,m+1,e,l,r);

    return min(l_a,r_a);
}
int main(){
    int n,q,arr[100005],i;
    scanf("%d%d",&n,&q);
    for(i=1;i<=n;i++) scanf("%d",&arr[i]);

    build(1,1,n,arr);

    while(q--){
        int b,c;
        scanf("%d%d",&b,&c);
            printf("%d\n",query(1,1,n,b+1,c+1));
    }

    return 0;
}
