#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
    int a[100],i,n,b,m;
    for(i=0;i<100;i++)
    {
        a[i]=0;
    }
    printf("enter the number of elements you want to input");
    scanf("%d",&m);
    for(i=0;i<m;i++)
    {
        printf("input the number ");
        scanf("%d",&n);
        b=n%100;
        if(a[b]==0)
        {
             a[b]=n;
             printf("%d is input at position %d",a[b],b);
        }
        else
        printf("data collision");
    }
}
