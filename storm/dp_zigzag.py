
n = input()
numbers = map(int, raw_input().split(","))

dp = [0] * (n)

for i in range(n):
	
	if i == 0:
		dp[i] = 1
		lastDiffIsPositive = True

	else:		
		prev = numbers[i-1]
		curr = numbers[i]
		diff = prev - curr
				
		if (diff >= 0 and not lastDiffIsPositive) or (diff < 0 and lastDiffIsPositive):
			dp[i] = dp[i-1] + 1
						
		else:
			dp[i] = dp[i-1]
			
		lastDiffIsPositive = (diff >= 0)			
		
print dp[-1]

























#n = input()
#numbers = map(int, raw_input().split(","))

#dp = [0] * (n)

#for i in range(n):
	
	#if i == 0:
		#lastDiffIsPositive = True

	#else:		
		#prev = numbers[i-1]
		#curr = numbers[i]
		#diff = prev - curr
				
		#if (diff >= 0 and not lastDiffIsPositive) or (diff < 0 and lastDiffIsPositive):
			#dp[i] = dp[i-1] + 1
						
		#else:
			#dp[i] = dp[i-1]
			
		#lastDiffIsPositive = (diff >= 0)			
		
#print dp[-1]
