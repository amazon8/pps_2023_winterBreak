#include <algorithm>
#include <iostream>

using namespace std;

/*
1. 계산
*/

long long totalPrice, t, sum, a, b;
int main(){
    cin >> totalPrice >> t;
    while(t--){
        cin >> a >> b;
        sum += a * b;
    }
    if(totalPrice == sum){
        cout << "Yes";
    }
    else{
        cout << "No";
    }
}