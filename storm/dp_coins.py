# coding: utf-8

# LINK TO PROBLEM:
# https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-find-a-solution/#dp
# https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

#	Given a list of N coins with their values (V1, V2, … ,VN), and the total sum S. 
#	Find the minimum number of coins the sum of which is S (you can use as many 
#	coins of one type as you want), or report that it’s not possible to select 
#	coins in such a way that they sum up to S.

#	Let N <= 1,000 and S <= 1,000.


n = int(raw_input())
s = input()
coins = map(int, raw_input().split())

dp = [float('Inf')] * (s+1)
dp[0] = 0

for i in xrange(1, s+1, 1):
	for j in range(n):
		
		m = dp[i-coins[j]]
		if (coins[j] <= i and m + 1 < dp[i]):
			dp[i] = m + 1
		
print dp[s]
