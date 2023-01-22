#include <algorithm>
#include <iostream>

/*
1. 1부터 뺌
2. 
*/

using namespace std;

int main(int argc, const char * argv[]) {
    long long S;
    int num = 1;
    int cnt = 0;
    long long sum = 0;
    
    cin >> S;
    while(1){
        sum += num;
        cnt++;
        if(sum > S){
            cnt--;
            break;
        }
        num++;
    }
    cout << cnt << '\n';
    return 0;
}