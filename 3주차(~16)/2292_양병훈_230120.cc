#include <algorithm>
#include <iostream>

/*
1. 뺄셈 --> 1, 6, 12, 19
*/

using namespace std;

int main() {
    int number;
    cin >> number;
    int i = 0;
    for(int sum=2; sum <= number; i++)
        sum += 6*i;
    if(number == 1) i=1;
    cout << i;
    return 0;
}