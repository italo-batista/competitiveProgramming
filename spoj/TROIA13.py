# coding: utf-8
# PROBLEM: http://br.spoj.com/problems/TROIA13/

import sys
sys.setrecursionlimit(10000)

# DFS

def dfs(i):
	visited[i] = True
	for adj in grafo[i]:		
		if not visited[adj]:
			dfs(adj)


# INICIALIZA

n, m = map(int, raw_input().split())
grafo   = [[] for j in xrange(n+10)]
visited = [False for i in xrange(n+10)]

for i in xrange(m):
	y, x = map(int, raw_input().split())
	y = y -1;
	x = x -1;
	grafo[y].append(x)
	grafo[x].append(y)
		
		
# MAIN

n_components = 0
for index in xrange(n):	
	if not visited[index]:		
		n_components += 1
		dfs(index)


print n_components

# NÂO PASSOU GGGRRRR
