# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/152/C

n, m = map(int, raw_input().split())


matriz = []
for i in xrange(n):
	
	word = str(raw_input())
	
	for j in xrange(m):
		
		if len(matriz) == j:
			matriz.append([])
		
		if word[j] not in matriz[j]:
			matriz[j].append(word[j])

s = 1
for i in xrange(m):
	s *= len(matriz[i])
	s = s % 1000000007
	
print s
