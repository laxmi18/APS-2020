#include <stdio.h>
#include <string.h>

int main(){
	char s[1000],r[1000];
	int l;
	scanf("%s",s);
	l = strlen(s);
	int c=0;
	for(int i=0;i<l/2;++i){
		if(s[i]==s[l-i-1])
		c++;
	}
	if(c==l/2){
		printf("YES");
	}
	else
	printf("NO");
	return 0;
}
