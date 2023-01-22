#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 40 미만 --> 40
2. 평군
*/

using namespace std;

 
int main(int argc, char const *argv[]) {

  int score, sum=0;
  for(int i=0; i<5; i++)
  {  
    cin >> score;
    if(score<40) sum += 40;
    else sum += score;
  }

  cout << sum/5 << endl;
	
}
