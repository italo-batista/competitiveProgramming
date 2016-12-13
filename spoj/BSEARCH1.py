# LINK FOR PROBLEM: http://www.spoj.com/problems/BSEARCH1/

def binarySearch(key, i, j):
	
	if i > j or array[i] > key or array[j] < key:
		return -1
	
	else:	
		mid = (i + j) / 2
		
		if array[mid] == key:
			return findLowerIndex(mid, key, i)
			
		elif array[mid] < key:
			return binarySearch(key, mid+1, j)
			
		else:
			return binarySearch(key, i, mid-1)
		
def findLowerIndex(currentI, key, i):
	tempI = currentI

	while tempI > i and array[tempI] == array[tempI-1]:
		tempI = tempI -1

	return tempI
	
	
n, queries = map(int, raw_input().split())

array = map(int, raw_input().split())

for i in range(queries):
	
	q = int(raw_input())
	
	print binarySearch(q, 0, len(array)-1)
	
	
	
	
