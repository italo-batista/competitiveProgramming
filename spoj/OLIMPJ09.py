# LINK FOR PROBLEM: http://br.spoj.com/problems/OLIMPJ09/
# LINKS THAT HELPED: 
#	http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
#	http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/

from operator import itemgetter 

def getKey(item):
	return (item[1], -item[0])

n, m =  map(int, raw_input().split())

paises = [()] * (n + 1)

for i in range(0, n+1, 1):
	paises[i] = (i, 0)

for i in range(m):
	o, p, b = map(int, raw_input().split())
	
	index = paises[o][0]
	freq  = paises[o][1]
	paises[o] = (index, freq + 1)

	index = paises[b][0]
	freq  = paises[b][1]	
	paises[b] = (index, freq + 1)
	
	index = paises[p][0]
	freq  = paises[p][1]
	paises[p] = (index, freq + 1)

paises.pop(0)
paises.sort(key=getKey, reverse=True)

ans = ""
for i in range(n):
	ans = ans + str(paises[i][0]) + " "
ans = ans[0:len(ans)-1]

print ans
