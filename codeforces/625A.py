# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/625/A

n = int(raw_input())
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
t = 0

if (b-c) < a:
	while n - b >= 0:
		qnt = (n-c) / (b-c)
		t +=  qnt
		n -= qnt * b
		n += qnt * c
		
qnt = n / a
t += qnt
		
print t
