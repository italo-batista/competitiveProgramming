#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define MAX 2001

using namespace std;

int t, m, n, tam1, tam2, dp[MAX][MAX];
string str_one, str_two;

int my_min(int a, int b, int c) {
   return min(min(a, b), c);
}

int main() {
		
	// dp[all i] = -1		
	memset(dp, -1, sizeof(dp)); 
	
	cin >> t;
	
	for (int caso_de_teste = 0; caso_de_teste < t; caso_de_teste++) {
		
		cin >> str_one; 
		cin >> str_two;
		
		m = str_one.length();
		n = str_two.length();
		
		for (int i=0; i<=m; i++) {	
			tam1 = i;
			
			for (int j=0; j<=n; j++) {
				tam2 = j;
				
				if (tam1 == 0)
					dp[tam1][tam2] = tam2;

				else if (tam2 == 0) 
					dp[tam1][tam2] = tam1;
					
				else if (str_one[tam1-1] == str_two[tam2-1])
					dp[tam1][tam2] = dp[tam1-1][tam2-1];
					
				else {				
					int removing  = dp[tam1-1][tam2];
					int adding    = dp[tam1][tam2-1];
					int replacing = dp[tam1-1][tam2-1];
	
					dp[tam1][tam2] = 1 + my_min(adding, removing, replacing);				

				} // end else							
			} // end inner for
		} // end for
				
		cout << dp[m][n] << "\n";
	}

	return 0;
}

// PROBLEM DEFINED HERE:
// http://www.spoj.com/problems/EDIST/
