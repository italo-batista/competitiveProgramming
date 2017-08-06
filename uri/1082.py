# coding: utf-8
# PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1082

import sys
sys.setrecursionlimit(10000)

l2n = {
'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 
'f':5, 'g':6, 'h':7, 'i':8, 'j':9,
'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
'p':15, 'q':16, 'r':17, 's':18, 't':19,
'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
 
n2l = {
0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 
5:'f', 6:'g', 7:'h', 8:'i', 9:'j',
10:'k', 11:'l', 12:'m', 13:'n', 14:'o',
15:'p', 16:'q', 17:'r', 18:'s', 19:'t',
20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}


# DFS

def dfs(i):
	visited[i] = True
	my_components.append(n2l[i])
	for adj in grafo[i]:		
		if not visited[adj]:
			dfs(adj)



n = input()

for teste in range(n):

	v, e = map(int, raw_input().split())
	grafo   = [[] for j in xrange(v)]
	visited = [False for i in xrange(v)]	

	
	# INICIALIZA GRAFO

	for i in xrange(e):
		y, x = map(str, raw_input().split())
		
		y = l2n[y]
		x = l2n[x]
		grafo[y].append(x)
		grafo[x].append(y)
						
	
	# MAIN

	n_components = 0
	components = []
	for index in xrange(v):	
		if not visited[index]:		
			my_components = []
			n_components += 1
			dfs(index)
			components.append(my_components)
			
	components = sorted(components, key=lambda x: x[0])			
				
	print "Case #%d:" % (teste+1)
	for component in components:
		component = sorted(component, key=lambda x: x[0])
		print ','.join(str(x) for x in component) + ","

	print n_components, 'connected components'
	print ""

