#include <bits/stdc++.h>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

#define MAX 4000

using namespace std;

int n, s, peso[MAX], valor[MAX], dp[MAX][MAX];

int knapsack(int obj, int aguenta) {
	
	if (dp[obj][aguenta] >= 0) {
		return dp[obj][aguenta];
	}
	
	if (obj > n || aguenta == 0) {
		return 0;
	}
	
	int n_coloca; // maior valor que podemos obter sem colocar obj na mochila
	n_coloca = knapsack(obj+1, aguenta);
	
	if (peso[obj] <= aguenta) {
		int coloca; // maior valor que podemos obter colocando obj na mochila
		coloca = valor[obj] + knapsack(obj+1, aguenta-peso[obj]);
		
		return dp[obj][aguenta] = max(coloca, n_coloca);
	}
	
	// nao entrou no if acima -> nao era possivel colocar obj
	return dp[obj][aguenta] = n_coloca;
}

int main(){
	
	memset(dp, -1, sizeof(dp)); // dp[all i] = -1
	
	cin >> s >> n;
	
	for(int i=1; i<=n; i++) {
		cin >> peso[i] >> valor[i];	
	}

	cout << knapsack(1, s);
	return 0;
}


// PROBLEM DEFINED HERE:
//	http://noic.com.br/informatica/curso-noic-de-informatica/aula-13-programacao-dinamica/
