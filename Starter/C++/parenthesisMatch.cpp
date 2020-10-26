#include <iostream>
#include <string>
using namespace std;

struct stack {
	int top;
	int capacity;
	char* arr;
};
int isfull(struct stack* head) {
	if (head->top == (head->capacity) - 1)
		return 1;
	else
		return 0;
}
int isempty(struct stack* head) {
	if (head->top == -1)
		return 1;
	else
		return 0;
}

void push(struct stack* head, char a) {
	if (isfull(head))
		cout << "overflow";
	else {
		head->top++;
		head->arr[head->top] = a;
	}
}

void pop(struct stack* head) {
	if (isempty(head))
		cout << "underflow";
	else {
		char data = head->arr[head->top];
		head->top--;
	}
}

int matching(string s) {
	struct stack* sp = new struct stack;
	int l = s.length();

	sp->top = -1;
	sp->capacity = l;
	sp->arr = new char[l];

	for (int i = 0; i < l; i++) {
		if (s[i] == '(') {
			push(sp, '(');
		}
		else if (s[i] == ')') {
		if (isempty(sp))
			return 0;
		else
			pop(sp);
		}
	}
	if (isempty(sp))
		return 1;
	else
		return 0;
}

int main() {

	string s;
	cin >> s;

	if (matching(s))
		cout << "matching";
	else
		cout << "not matching";

	return 0;
}
