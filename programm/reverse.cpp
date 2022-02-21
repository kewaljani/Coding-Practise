#include<stdio.h>
#include<iostream>

int main()
{
	int rev = 0;
	int num = 123;
	while(num!=0)
	{
	rev = (rev*10)+(num%10);
	num = num/10;
	}
	std::cout<<rev;
return 0;
}
