

## CONSTRUCTING GRAPH

v, e = map(int, raw_input().split())

grafo = [[] for i in range(v+1)]

for i in range(e):
        v1, v2, w = map(int, raw_input().split())
        # save edges that are getting in me, not edges from me to another v
        grafo[v2].append((v1, w))


## INITIALIZING

beginning = input()
dp = [[float('inf') for i in range(v+1)] for j in range(v+1)]       
for i in range(v+1): dp[i][beginning] = 0


## BELLMAN-FORD MAIN

for i in range(1, v+1, 1):
	for j in range(1, v+1, 1):
	
		sub_paths = [float('inf')]		
		for adj in grafo[j]:
			adj_index = adj[0]
			adj_weigth = adj[1]			
			sub_paths.append( dp[i-1][adj_index] + adj_weigth )
		
		min_weigth_sub_path = min(sub_paths)
		dp[i][j] = min(dp[i-1][j], min_weigth_sub_path)
