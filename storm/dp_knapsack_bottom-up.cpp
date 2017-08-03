#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define MAX 4000

using namespace std;

int n, s, peso[MAX], valor[MAX], dp[MAX][MAX];

int main() {
	
	memset(dp, -1, sizeof(dp)); // dp[all i] = -1
	
	cin >> s >> n;
	for (int i=1; i<=n; i++) {
		cin >> peso[i] >> valor[i];	
	}
	
	
	// knapsack algo
	
	for (int i=0; i<=n; i++) {
		
		int obj = i;
		
		for (int j=0; j<=s; j++) {
			
			if (i == 0 || j == 0) dp[obj][j] = 0;
			
			else {
			
				int aguenta = j;
				
				int n_coloca = dp[obj-1][aguenta];
				
				if (peso[obj] <= aguenta) {
					int coloca = valor[obj] + dp[obj-1][aguenta-peso[obj]];
					dp[obj][aguenta] = max(coloca, n_coloca);
				
				} else {
					dp[obj][aguenta] = n_coloca;			
				}
			}
		}		
	}

	cout << dp[n][s];
	return 0;
}
