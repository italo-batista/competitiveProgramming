#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>

#define MAX 1000000

using namespace std;

int n, dp[MAX];

int fib(int x) {
	
	if (dp[x]!= -1) return dp[x];
	
	if (x == 0) return 1;
	if (x == 1) return 1;
		
	return dp[x] = fib(x-1) + fib(x-2);
}

int main(){
	
	memset(dp, -1, sizeof(dp)); // dp[all i] = -1
	
	cin >> n;
	cout << fib(n);
	
	return 0;
}
