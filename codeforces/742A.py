
# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/742/A

n = int(raw_input())

if n == 0:
	print '1'
else:
	factor = n % 4

	if factor == 1:
		print '8'
	elif factor == 2:
		print '4'
	elif factor == 3:
		print '2'
	else:
		print '6'
