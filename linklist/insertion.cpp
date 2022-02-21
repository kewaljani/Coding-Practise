#include<stdio.h>
#include<iostream>
using namespace std;
class Node
{
	public:
	int data;
	Node* next;
};


void push(Node** head, int x)
{
	Node* newnode = new Node();
	newnode->data = x;
	newnode->next = (*head);
	(*head) = newnode;	
	
}



int main()
{
	Node* head= NULL;
	head = new Node();
	push(&head,10);
	cout<<head->data;
	return 0;
}
