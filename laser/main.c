/*#include <stdio.h>
#include <stdlib.h>

int main()
{
    int t;
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        int n,q;
        scanf("%d %d",&n,&q);
        int query[n+1];
        query[0]=0;
        for (int j=1;j<=n;j++){
            scanf("%d",&query[j]);
        }
        for (int j=0;j<q;j++){
            int x1,x2,y;
            int c=0;
            scanf("%d %d %d",&x1,&x2,&y);
            for(int k=1;k<n;k++){
                float m= query[k+1]-query[k];
                float c = -(query[k+1]-query[k])*k + query[k];
                float x = (y-c)/m;
                printf("%f %f %f\n",m,c,x);
                if(x>=j && x<=j+1 && x<=x2 && x>=x1){
                    c++;
                }
            }
            printf("%d\n",c);
        }
    };
    return 0;
}
*/
// C program to illustrate _builtin_popcount(x)

#include <stdio.h>
int main()
{
    int t,n,q,p,odd,even;
    scanf("%d",&t);
    while(t){
        scanf("%d %d",&n,&q);
        odd=0;
        even=0;
        int a[n];
        for(int j=0;j<n;j++){
                scanf("%d", &a[j]);
            if(__builtin_parityll(a[j])){
                odd++;
            }
            else
                even++;
    }
    for(int i=0;i<q;i++){
        scanf("%d",&p);
        if(__builtin_parityll(p))
            printf("%d %d\n",odd,even);
        else
            printf("%d %d\n",even,odd);
    }
    t--;
    }
	return 0;
}
