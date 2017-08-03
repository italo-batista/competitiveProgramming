#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>

#define MAX 1000000

using namespace std;

int n, dp[MAX];

int main(){

	dp[0] = dp[1] = 1;
	
	cin >> n;
	
	for(int i=2; i <= n+1; i++) {
		dp[i] = dp[i-1] + dp[i-2];
	}
		
	cout << dp[n];
		
	return 0;
}
