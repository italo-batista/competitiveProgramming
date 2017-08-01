MAX = 100
n = int(raw_input())

while n != 0:
		
	valores = [0] * (n+1)
	pesos = [0] * (n+1) 

	for i in xrange(n):	
		p, P = map(int, raw_input().split())
		valores[i] = p
		pesos[i] = P
		
	m = int(raw_input())
		
	dp = []
	for i in xrange(n+1):
		array = []
		for j in xrange(m+1):
			array.append(0)
		dp.append(array)
					
	for i in xrange(n+1):
		for j in xrange(m+1):
							
			if i == 0 or j == 0:
				dp[i][j] = 0

			elif j < pesos[i-1]:
				dp[i][j] = dp[i-1][j]
				
			else:
				sol1 = dp[i-1][j]
				sol2 = dp[i-1][j - pesos[i-1]] + valores[i-1]
				
				dp[i][j] = max(sol1, sol2)
				
	print dp[n][m]		
	n = int(raw_input())
