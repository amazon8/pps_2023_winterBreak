#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 햄버거 중 max, 음료수
2. 
*/

using namespace std;

int main(int argc, char const *argv[]) {
 
  int h1, h2, h3, b1, b2, hMin, bMin;

  cin >> h1;
  cin >> h2;
  cin >> h3;
  cin >> b1;
  cin >> b2;

  hMin = min(h1, h2);
  hMin = min(hMin, h3);
  bMin = min(b1, b2);

  cout << hMin + bMin - 50 << endl;
  
}