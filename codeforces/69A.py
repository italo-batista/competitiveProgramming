# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/69/A

n = int(raw_input())

xf = 0
yf = 0
zf = 0

for i in range(n):
	ent = map(int, raw_input().split())

	x = ent[0]
	y = ent[1]
	z =	ent[2]

	xf += x
	yf += y
	zf += z
	
if (xf == 0) and (yf == 0) and (zf == 0):
	print "YES"
else:
	print "NO"
