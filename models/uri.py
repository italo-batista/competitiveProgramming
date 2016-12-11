# n, x, y = map(int, raw_input().split())

import math

m = 10 ** 3 + 10

crivo = [True] * m

crivo[0] = False
crivo[1] = False

for i in xrange(int(math.sqrt(m))):
	
	if crivo[i]:
		
		for j in xrange(i*i, m, i):
			crivo[j] = False

primos = []
for i in range(len(crivo)):
		if crivo[i]:
			primos.append(i)
			

n = int(raw_input())

count = 0
guesses = ""
for i in range(len(primos)):
	
	j = 1
	while (j <= n/(i+1)):
		j = j * primos[i]
		guesses += str(j) 
		guesses += " "
		count += 1

print count,
print guesses
