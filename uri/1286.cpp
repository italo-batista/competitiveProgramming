#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define MAX 35

using namespace std;

int n, p, tempo[MAX], qnt_pizza[MAX], dp[MAX][MAX];

int motoboy(int obj, int aguenta) {
	
	if (dp[obj][aguenta] >= 0) {
		return dp[obj][aguenta];
	}
	
	if (obj > n || aguenta == 0) {
		return 0;
	}
	
	int n_coloca; // maior valor que podemos obter sem colocar obj na mochila
	n_coloca = motoboy(obj+1, aguenta);
	
	if (qnt_pizza[obj] <= aguenta) {
		int coloca; // maior valor que podemos obter colocando obj na mochila
		coloca = tempo[obj] + motoboy(obj+1, aguenta-qnt_pizza[obj]);
		
		return dp[obj][aguenta] = max(coloca, n_coloca);
	}
	
	// nao entrou no if acima -> nao era possivel colocar obj
	return dp[obj][aguenta] = n_coloca;
}

int main() {
	
	cin >> n;
	while ( n != 0 ) {
		
		cin >> p;
		
		// dp[all i] = -1
		memset(dp, -1, sizeof(dp));
		
		for (int i=1; i<=n; i++) {
			cin >> tempo[i] >> qnt_pizza[i];	
		}		
		
		cout << motoboy(1, p) << " min.\n";
		cin >> n;		
	}
	
	return 0;
}
