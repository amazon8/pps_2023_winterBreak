#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
/*
1. 피타고라스
2. 
*/

using namespace std;

 
long long term[1000];
long long dp(int n) {
	
	if(n == 0 or n == 1 or n == 2) return 1;
	
	if(term[n] != 0) return term[n];
	
	else {
		term[n] = dp(n-2) + dp(n-3);
		return term[n];
	}
}

int main() {
	int t;
	int n;
	cin >> t;
	
	
	for(int i=0; i<t; i++) {
		cin >> n;
		cout << dp(n-1) << endl;
	}

}