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

int d(int number) {
	int sum = number;
 
	while (number != 0) {
		sum = sum + (number % 10); // 첫 째 자리수ˇ
		number = number / 10;	   // 10을 나누어 첫 째 자리를 없앤다.
	}
	return sum;
}
 
 
int main(int argc, char const *argv[]) {
	bool check[10001] = { false, };
	for (int i = 1; i < 10001; i++) {
		int n = d(i);
		if (n < 10001) { // 10000 이 넘는 수는 필요가 없다.
			check[n] = true;
		}
	}
	for (int i = 1; i < 10001; i++) {
		if (!check[i]) {
			cout << i << "\n";
		}
	}
 
	return 0;
}
