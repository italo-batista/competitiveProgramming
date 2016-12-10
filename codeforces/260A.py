# LINK FOR PROBLEM:  http://codeforces.com/problemset/problem/260/A
a,b,n = map(int, raw_input().split())

a = a * 10
flag = False
		
for j in range(10):
		
	temp = a + j
		
	if temp % b == 0:
		a = temp
		flag = True
		break
			
if flag:
	
	a = str(a)
	for i in range(n-1):
		a = a + "0"
	
	print a
else:
	print -1
