# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/660/A

def MDC(a,b):
	while (a % b != 0):
		aux = b
		b = a % b
		a = aux
	return b

n = int(raw_input())
ent = map(int, raw_input().split())

temp = ""
k = 0

if n > 1:

	for i in range(n-1):

		temp = temp + str(ent[i]) + " "
		
		mdc = MDC( ent[i], ent[i+1])
		if mdc != 1:
			temp = temp + str(1) + " "
			k = k + 1

	temp = temp + str(ent[i+1])
	
	print k
	print temp 	

else:
	print 0
	print ent[0]
