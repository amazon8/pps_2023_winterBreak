#include <iostream>

using namespace std;

/*
1. 해당 위치에서 4가지 빼고 가장 작은 경우
*/


int main() {

  int x,y,w,h;
  int tmp1,tmp2;
  cin >> x >> y >> w >> h;
  tmp1 = min(x,y);
  tmp2 = min(w-x,h-y);
  cout << min(tmp1,tmp2);
  
}