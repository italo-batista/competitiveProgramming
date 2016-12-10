# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/734/A

n = int(raw_input())
p = str(raw_input())

a = 0
d = 0

for i in range(n):
	if p[i] == "A":
		a += 1
	elif p[i] == "D":
		d += 1

if a > d:
	print "Anton"
elif d > a:
	print "Danik"
else:
	print "Friendship"
