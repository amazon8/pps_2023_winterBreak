#include <algorithm>
#include <iostream>


/*
1. 한 시험장 별로 인원 더하기
*/

using namespace std;
int N, A[1000001], B, C;
long long sum;


int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
	}

	cin >> B >> C;

	for (int i = 0; i < N; i++)
	{
		// 총감독관 한명으로 응시생 모두를 커버할 수 있을 때
		if (A[i] <= B) sum++;
		// 총감독관 한명이 감시할 수 있는 응시생 수를 제외하고
		// 필요한 부감독관의 수 계산
		else
		{
			sum += (A[i] - B) / C + 1;

			// ex 2명을 감시할 수 있는 부감독관은
			// 3명일때는 2명이 필요하기 때문 
			if ((A[i] - B) % C != 0) sum++;
		}	
	}
	cout << sum;
}