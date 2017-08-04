# coding: utf-8

s1 = str(raw_input())
s2 = str(raw_input())

N = len(s1)
M = len(s2)

dp = [[0 for i in range(M+1)] for j in range(N+1)]
	
for i in xrange(1, N+1, 1):
	for j in xrange(1, M+1, 1):
		
		print i, j
		
		if s1[i-1] == s2[j-1]:
			dp[i][j] = 1 + dp[i-1][j-1]
		
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
							
print dp[i][j]
