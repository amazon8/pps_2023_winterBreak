#include <iostream>
#include <algorithm>


using namespace std;

/*
1. for 문 f_fib, s_fib
*/

int memo[100] = { 0, };
int fib(int n)
{
	
	if (n <= 1)
		return n;

	if (memo[n] > 0)
		return memo[n];

	memo[n] = fib(n - 1) + fib(n - 2);
		return memo[n];
	
}

int main()
{
	
	int n;
	cin >> n;


	cout << fib(n);

}