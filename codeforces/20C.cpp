#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

#define MAX 110010
#define ll unsigned long long int
#define p pair<ll,ll>
#define append push_back

vector<p> grafo[MAX];
ll distances[MAX], pares[MAX];
int n, m, x, y;
ll peso;

void dijkstra() {

    distances[1] = 0;
    priority_queue<p> queue;
    queue.push(make_pair(0, 1));

	while(!queue.empty()) {

		int top = queue.top().second;
		ll dist = -queue.top().first;
		queue.pop();

		if (dist == distances[top]) {

			for(int i = 0; i < grafo[top].size(); i++) {

				int no = grafo[top][i].first;
				ll peso = grafo[top][i].second;

				if (distances[no] == -1 || distances[no] > dist + peso) {
					distances[no] = dist + peso;
					queue.push(make_pair(-distances[no], no));
					pares[no] = top;
				}
			}
		}
	}
}

void printPares() {

	if(distances[n] == -1) {
		printf("-1\n");
		return;
	}

    int temp = n;
    vector<int> ans;

    while(temp != 1) {
        ans.append(temp);
        temp = pares[temp];
    }

    printf("%d ", 1);
    for(int i = ans.size() - 1; i >= 0; i--) {
		printf("%d ", ans[i]);
	}
}

int main() {

    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        scanf("%d %d %lld", &x, &y, &peso);
        grafo[x].append(make_pair(y, peso));
        grafo[y].append(make_pair(x, peso));
    }

    for(int i = 0; i < MAX; i++) {
        distances[i] = -1;
        pares[i] = -1;
    }

    dijkstra();
    printPares();

    return 0;
}