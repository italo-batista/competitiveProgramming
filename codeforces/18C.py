# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/18/C

n = int(raw_input())
ent = map(int, raw_input().split())

soma_t = sum(ent)
soma_p = 0
count = 0

for i in range( n - 1 ):
	soma_p = soma_p + ent[i]
	soma_t = soma_t - ent[i]
	
	if soma_p == soma_t:
		count = count + 1

print count
