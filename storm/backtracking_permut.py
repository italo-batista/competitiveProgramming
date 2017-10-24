# coding:utf-8

# Use Backtracking para gerar todas as permuta̧c̃oes de um array a.
# Restri̧c̃oes: sj != sk para todo sj

,sk ∈ S e todo j 6= k

def podeBotar(parcial):
	tam = len(parcial)
	
	for j in range(0, tam-1):
		if parcial[j] == parcial[tam-1]:
			return False
	return True

def perm(parcial, possiveis, n):
	
	i = len(parcial)
	
	if i == n:
		print parcial
	
	else:
		for p in possiveis:
				
			partial = parcial + [p]
									
			if podeBotar(partial):				
				perm(partial, possiveis, n)

		

a = map(int, raw_input().split())
n = len(a) # tam que a solução deve ter

x = []
perm(x, a, n)
