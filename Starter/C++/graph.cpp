#include<iostream>
using namespace std;
void check(int n,int adj[n+1][n+1],int x,int y)
{
    if(adj[x][y]==1)
    cout<<"There is a link between them "<<endl;
    else cout<<"There is no link between the given two"<<endl;
}
int main()
{
    int n;
    cout<<"Enter the number of nodes"<<endl;
    cin>>n;
    cout<<"Enter the number of links"<<endl;
    int x;
    cin>>x;
    int adj[n+1][n+1];
    for(int i=0;i<n+1;i++)
    {
        for(int j=0;j<n+1;j++)
        {
            adj[i][j]=0;
        }
    }
    cout<<"Enter the node between which you want to create link"<<endl;
    for(int i=0;i<x;i++)
    {
        int o,p;
        cin>>o>>p;
        adj[o][p]=1;
    }
    cout<<"Enter the node between which you want to check the link"<<endl;
    int y,z;
    cin>>y>>z;
    check(n,adj[][],y,z);

    return 0;
}