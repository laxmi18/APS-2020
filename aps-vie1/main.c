#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, m[50][50],w[50][50],i,j,q,id[50];
    scanf("%d",&n);
    int free_men[10],free_women[10];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&m[i][j]);
        }
        free_men[i] = 0;
    }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&w[i][j]);
        }
        free_women[i] = 0;
    }
    scanf("%d",&q);
    for(i=0;i<q;i++){
        scanf("%d",&id[i]);
    }
    int c = 0;
    for(i=0;i<n;i++){
        if(!free_men[i]){
            for(j=0;j<n;j++){
                if(free_women[j]==0 && m[i][j]==1){
                    printf("%d accepted %d proposal\n",w[i][j],m[i][j]);
                    free_women[j] = 1;
                }
                else if(free_women[j]==1 && w[i][j] < w[i][free_women[j]]){
                    printf("%d accepted %d proposal\n",w[i][j],m[i][j]);
                    free_women[j] = 1;
                }
            }
            free_men[i] = 1;
        }

    }
}
