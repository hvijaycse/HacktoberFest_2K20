#include<iostream>
using namespace std;
class a
{
public:
void display{
cout<<"base class";
}};
class b{
public:
void display(){
cout<<"derived class";
}};
int main()
{
b obj;
obj.display();
return 0;
}