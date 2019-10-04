#include<stdio.h>
void merge(int a[],int l,int r){
    if(l<r){
        int m = (l+r)/2;
        merge(a,l,m);
        merge(a,m+1,r);
        sort(a,l,m,r);
    }
}
void sort(int a[],int l,int m,int r){
    int n1 = m-l+1;
    int n2 = r-m;
    int L[n1], R[n2];
    int i,j,k;
    for(i=0;i<n1;i++){
        L[i]=a[i+l];
    }
    for(j=0;j<n2;j++){
        R[j]=a[j+m+1];
    }
    i=0;j=0;k=l;
    while(i<n1 && j<n2){
        if(L[i]<=R[j]){
            a[k]=L[i];
            i++;
        }else{
            a[k]=R[j];
            j++;
        }
        k++;
    }
    while(i<n1){
        a[k]=L[i];
        i++;
        k++;
    }
    while(j<n2){
        a[k]=R[j];
        j++;
        k++;
    }
}
void print(int a[],int n){
    int i;
    for(i=0;i<n;i++){
        printf("%d\n",a[i]);
    }
}
int main(){
    int a[] = {2,3,8,1,9,7,4,5,0};
    int n = sizeof(a)/sizeof(a[0]);
    printf("Array before sorting \n");
    print(a,n);
    merge(a,0,n-1);
    printf("Array after sorting\n");
    print(a,n);
}