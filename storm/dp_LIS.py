# coding: utf-8

sequence = map(int, raw_input().split())

N = len(sequence)
dp = [1] * (N+1)

ans = 0
for i in xrange(N):	
	dp[i] = 1
	
	for j in xrange(i):		
		if (sequence[j] < sequence[i] and dp[i] <= dp[j]):
			dp[i] = dp[j] + 1
		
	if (ans < dp[i]):
		ans = dp[i]
		
print ans


