# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/735/A

n, k = map(int, raw_input().split())

seq = str(raw_input())

gi = 0
ti = 0
i = 0
while i < (n):
	if seq[i] == "G":
		gi = i
	if seq[n-i-1] == "T":
		ti = n-i-1
		
	i = i + 1
	
	if gi != 0  and ti != 0:
		break

if gi < ti:
	while gi <= ti:

		if seq[gi] == "#":
			break
		elif seq[gi] == "T":
			print "YES"
			break
		else:
			gi = gi + k
else:
	while gi >= ti:
	
		if seq[gi] == "#":
			break
		elif seq[gi] == "T":
			print "YES"
			break
		else:
			gi = gi - k


if gi != ti:
	print "NO"

