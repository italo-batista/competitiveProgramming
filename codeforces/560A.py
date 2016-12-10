# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/560/A


def MDC(a,b):
	while (a % b != 0):
		aux = b
		b = a % b
		a = aux
	return b
	
def MMC(a, b):
	return a / MDC(a, b) * b
	

n = int(raw_input())

ent = map(int, raw_input().split())

if 1 in ent:
	print -1
else:
	print 1
