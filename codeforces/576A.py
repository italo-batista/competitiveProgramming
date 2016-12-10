import math

# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/576/A

m = 10 ** 3 + 1

crivo = [True] * m

crivo[0] = False
crivo[1] = False

for i in xrange(int(math.sqrt(m))):
	
	if crivo[i]:
		
		for j in xrange(i*i, m, i):
			crivo[j] = False


n = int(raw_input())

guessing = []
for i in range(1,len(crivo),1):

	if crivo[i]:
		
		j = 1
		while (j <= n/(i)):
			j *= i
			if j not in guessing:
				guessing.append(j)


print len(frozenset(guessing))

guesses = ""
for i in range(len(guessing)):
	guesses += str(guessing[i])
	guesses += " "

print guesses[:len(guesses)-1]
