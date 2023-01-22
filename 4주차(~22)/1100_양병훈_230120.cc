#include <algorithm>
#include <iostream>

/*
1. 합 --> 짝수 흰, 홀수 검
2. 
*/

using namespace std;

char c;
int ans;

int main()
{
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			cin >> c;
			if((i + j) % 2 == 0 && c == 'F') ans++;
		}
	}
	cout << ans;
}