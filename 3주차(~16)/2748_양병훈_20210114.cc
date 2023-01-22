#include <iostream>

/*
1. for문 b --> t
*/

using namespace std;

int main() {

  long long num, firstF=0, secondF=1, res=0;
  
  cin >> num;

  if(num==0) cout << 0 << endl;
  else if(num==1) cout << 1 << endl;
  else
  {
    for(int i=1; i<num; i++)
    {
      res = firstF + secondF;
      firstF = secondF;
      secondF = res;
      
    }   
    cout << secondF << endl;
  }
  
  

}