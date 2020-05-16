#include<stdio.h>
int gcd(int a, int b)
{
 	if (a == 0)
 		return b;
 	return gcd(b%a, a);
}
void main()
{
	int minRange;
	int maxRange;
	int number;
	//code to scanf the three vars above
	int i, count=0,
	//code to test if minRange<=maxRange and generate error
	for(i=minRange; i<=maxRange; i++)
	{
		if(gcd(number,i)==1)
		{
			count++;
			printf("%d",i);
		}
	}
	(count == 0)?printf("No coprimes"):printf("%d coprimes generated");
}
