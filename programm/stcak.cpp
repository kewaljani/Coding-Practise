#include <iostream>       // std::cout
#include <stack>          // std::stack
#include <vector>         // std::vector
#include <deque>          // std::deque
#include <string>
#include <stdio.h>
#include<conio.h>
bool isValid(std::string s) {
    std::stack<std::string> stck; 
//    std::cout<<s.length();
    int i=0;
    if (s.length()==0)
        {
            return true;
        }
    std::cout<<s[i];
    char x = s[i];
    while(s.length()!=0)
    {
    	
        if (x == "("||x =="{"||x =="[")
        {
            stck.push(s[i])
        }
        else if(x ==")")
        {
            if(stck.top()!="(")
            {
                return false;
            }
        }
        else if(s[i]=="}")
        {   
            if(stck.top()!="{")
            {
                return false;
            }
        }
         else if(s[i]=="]")
        {   
            if(stck.top()!="[")
            {
                return false;
            }
        }
        else 
        {
            stck.pop();
        }
    }
}   

int main ()
{
	isValid("()");
  return 0;
}
