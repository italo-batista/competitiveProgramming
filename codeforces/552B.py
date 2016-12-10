# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/552/B

n = int(raw_input())

if n < 10:
	print 1 * (n + 1) - 1

elif n < 100:
	print 2 * (n + 1) - 11	

elif n < 1000:
	print 3 * (n + 1) - 111

elif n < 10000:
	print 4 * (n + 1) - 1111
	
elif n < 100000:
	print 5 * (n + 1) - 11111

elif n < 1000000:
	print 6 * (n + 1) - 111111
	
elif n < 10000000:
	print 7 * (n + 1) - 1111111

elif n < 100000000:
	print 8 * (n + 1) - 11111111

elif n < 1000000000:
	print 9 * (n + 1) - 111111111
	
else:
	print 10 * (n + 1) - 1111111111
