#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 윤년 조건
2. 
*/

using namespace std;

int main(int argc, char* argv[])
{
  int num;

  cin >> num;

  if(num%4==0)
  {
    if(num%100!=0)
    {
      cout << 1 << endl;
    }
    else if(num%400==0)
    {
      cout << 1 << endl;
    }
    else
    {
      cout << 0 << endl;
    }
  }
  else
  {
    cout << 0 << endl;
  }
  
}