#include<iostream>
#define MAX 4
//Stack works with LIFO principle 
int top=-1;
int a[MAX];


bool push(int x){
	if (top==MAX-1){
		std::cout<<"overflow"<<std::endl;
		return false;
	}
	else{
		top=top+1;
		a[top]=x;
		return true;
	}
}

int pop(){
	if(top==-1){
		std::cout<<"underflow";
	}
	else{
		int x=a[top];
		top=top-1;
		return 0;
	}
}
void maxelem(){
	int max=a[0];
	for(int i=0; i<=top;i++){
		if(a[i]>max){
			max=a[i];
		}
	}
	std::cout<<max;
}

void print(){
	int i;
	std::cout<<"elements are ";
	for(i=0; i<=top;i++){
		std::cout<<a[i]<<" ";
	}
}

int main(){
	int n;
	std::cin>>n;
	int a,d;
	for(int i=0; i<n;i++){
		std::cin>>a;
		switch(a){
			case 1:
				std::cin>>d;
				push(d);
				break;
			
			case 2:
				pop();
				break;
			
			case 3:
				maxelem();
				break;
			case 4:
				print();
				break;	
			default:
				std::cout<<"incorrect";			
		}
	}	
return 0;
}
