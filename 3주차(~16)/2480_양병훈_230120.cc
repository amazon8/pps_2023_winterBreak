#include <algorithm>
#include <iostream>

/*
1. sort
2. 비교 --> 계산
*/

using namespace std;

int main(int argc, char const *argv[]) {
 
	int a, b, c;
	cin >> a >> b >> c;
	// 만약 모든 변수가 다른 경우
	if (a != b && b != c && a != c) {
		int max;
		// 만약 a > b 라면
		if (a > b) {
			// c > a > b 라면
			if (c > a) {
				max = c;
			}
			// a > (b, c)
			else {
				max = a;
			}
		}
		// b > a 라면
		else {
			// c > b > a 라면
			if (c > b) {
				max = c;
			}
			// b > (a, c)
			else {
				max = b;
			}
		}
		cout << max * 100;
	}
	// 적어도 한 쌍 이상의 서로 같은 변수가 존재할 경우
	else {
		// 3개의 변수가 모두 같은 경우
		if (a == b && a == c) {
			cout << 10000 + a * 1000;
		} else {
			// a가 b혹은 c랑만 같은 경우
			if (a == b || a == c) {
				cout << 1000 + a * 100;
			}
			// b가 c랑 같은 경우
			else {
				cout << 1000 + b * 100;
			}
		}
	}
	return 0;
}