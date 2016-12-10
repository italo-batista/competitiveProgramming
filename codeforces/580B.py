# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/580/B
n, d = map(int, raw_input().split())

friends = []
for vez in xrange(n):
	
	m, s = map(int, raw_input().split())
	friends.append([m,s])

friends.sort()

most_friend_factor = 0
factor = 0
j = 0

for i in xrange(n):
	
	while j < n and (friends[j][0] - friends[i][0] < d):
		factor += friends[j][1]
		j += 1	
				
	if factor > most_friend_factor:
		most_friend_factor = factor

	factor -= friends[i][1]
	
			
				
print most_friend_factor

