#include<iostream>
#include<stdio.h>

class stack
	{
	
		int top = -1;
		public:
			int a[5000];
			bool push(int x);
			int pop();
			int peek();
			bool isEmpty();
	};
	
	bool stack::push(int x)
	{
		top++;	
		a[top] = x;
	}
	int stack::pop()
	{
		top--;
	}
	int stack::peek()
	{
		printf("%d",a[top]);
	}

int main()
{
	stack stack1;
	stack1.push(10);
	stack1.push(20);
	stack1.push(30);
	stack1.pop();
	stack1.peek();
	for(int i=0;i<2;i++)
	{
		printf("%d",stack1.a[i]);
	}
	return 0;
}
