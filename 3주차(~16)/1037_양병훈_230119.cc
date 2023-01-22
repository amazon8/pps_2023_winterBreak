#include <iostream>
#include <algorithm>


using namespace std;

/*
1. 정렬
2. 처음과 끝 곱하기
*/

int main() {

int tot; // 약수의 총 개수

	cin >> tot;
	int* div = new int[tot]; // 모든 약수
	
	for (int i = 0; i < tot; i++)
	{
		cin >> div[i];
	}

	sort(div, div+tot);

	cout << div[0] * div[tot - 1];
  
}