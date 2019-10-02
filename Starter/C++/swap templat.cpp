#include<iostream>

using namespace std;
 
template <class T>
  void swap1(T a,T b)
  {T temp=a;
  a=b;
  b=temp;
  	
  }
  
  int main()
  {
  	int i1,i2;
  	float f1,f2;
  	char c1,c2;
  	cin>>i1>>i2;
  	cin>>f1>>f2;
  	cin>>c1>>c2;
  	
  	swap1(c1,c2);
  	swap1(i1,i2);
  	swap1(f1,f2);
  	cout<<i1<<i2<<endl;
  	cout<<c1<<c2<<endl;
  	cout<<f1<<f2;
  	
  	return 0;
  }
