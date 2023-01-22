#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 분 비교
2. 시 비교
*/

using namespace std;

int main(void){
    int a, b;
    cin >> a >> b;
    if(b < 45){
        b += 15;
        a--;
    }
    else
        b -= 45;
    if(a < 0)
        a = 23;
    cout << a << " "<< b;
}
