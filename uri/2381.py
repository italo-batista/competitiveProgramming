# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/en/problems/view/2381

n, k =  map(int, raw_input().split())

nomes = []

for i in range(n):
	nome = str(raw_input())
	nomes.append(nome)
	
nomes.sort()

print nomes[k-1]
