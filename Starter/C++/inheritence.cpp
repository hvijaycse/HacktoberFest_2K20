#include<iostream>
using namespace std;

class Base{
	
	public:
	
	void fun()
	{
		cout<<"THIS IS IN BASE CLASS 1 \n ";
	}
};

class derived : public Base
{
	public:
	void funinderived(){
	cout<<"This is in Derived class 2 \n";
	}
	
};

class derived2 : public derived
{
	public:
	void funinderived2(){
	cout<<"This is in Derived class \n";
	}
	
};

int main()
{
	derived2 a;
	a.fun();
	a.funinderived();
	a.funinderived2();
	
	return 0;
}
