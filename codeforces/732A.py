# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/732/A

k,r = map(float, raw_input().split())
s = 0
c = 1

while True:
	
	s = k * c
	
	if (s % 10 == 0):
		print c
		break
	elif ( (s-r) % 10 == 0):
		print c
		break
	
	c += 1
	
