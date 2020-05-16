#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int a, int b)
{
    if(a >= b)
        return a;
    else
        return b;
}

int main()
{
    char s1[50],s2[50];
   // printf("Enter string1!\n");
    scanf("%s",s1);
    //printf("Enter string2!\n");
    scanf("%s",s2);
    int m = strlen(s1);
    int n = strlen(s2);
    int result[50][50],c=0;
    int i,j;
    result[0][0] = 0;
    for(i=1;i<=m;i++)
    {
        result[i][0] = 0;
        for(j=1;j<=n;j++)
        {
            result[0][j] = 0;
            if(s1[i-1]==s2[j-1])
               {
                   result[i][j] = result[i-1][j-1] + 1;
                   if(result[i][j] += 1)
                   {
                       printf("%c",s1[i-1]);
                   }
                   //c = 1;
               }
            else
                {
                    result[i][j] = max(result[i][j-1], result[i-1][j]);
                }
        }

    }
   /* for(i=0;i<=m;i++)
    {
        for(j=0;j<=n;j++)
        {
            printf("%d\t",result[i][j]);
        }
        printf("\n");
    }
*/
    return 0;
}
