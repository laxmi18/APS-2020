#include <stdio.h>

int main(void) {
	// your code goes here
	int T,i;
	long int N, C;
	scanf("%d",&T);
	while(T--){
	    scanf("%ld %ld",&N,&C);
	    int A[N],s=0;
	    for(i=0;i<N;i++){
	        scanf("%d",&A[i]);
	        s = s + A[i];
	    }
	    if(s<=C)
	    printf("YES\n");
	    else
	    printf("NO\n");
	}
	return 0;
}
