# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/315/B

def first(vi, xi):
	array[vi - 1] = xi
	
def sec(yi):
		
	i = 0
	j = len(array) - 1
	
	while i < j:

		array[i] = array[i] + yi
		array[j] = array[j] + yi
		
		i = i + 1
		j = j - 1
		
		
def third(qi):
	print array[qi-1]
	
	
INCR_FACTOR = 0
	
preent = map(int, raw_input().split())
array = map(int, raw_input().split())

n = preent[0]
m = preent[1]

for i in range(m):
	
	ent = map(int, raw_input().split())
	op = ent[0]
	
	if op == 1:
		
		vi = ent[1]
		xi = ent[2]
		array[vi - 1] = xi - INCR_FACTOR
		
	elif op == 2:
		
		INCR_FACTOR = INCR_FACTOR + ent[1]
		
	elif op == 3:
		
		qi = ent[1]
		print array[qi-1] + INCR_FACTOR
