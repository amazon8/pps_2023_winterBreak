#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 아스키
2. 
*/

using namespace std;

int main() {
    string k;
    cin >> k;
    for (int i = 0; i < k.size(); i++)
    {
        if (k[i] >= 97 && k[i] <= 122)
        {
            k[i] -= 32;
        }
        else if (k[i] >= 65&&k[i]<=90)
        {
            k[i] += 32;
        }
        cout << k[i];
    }
    cout << '\n';
}