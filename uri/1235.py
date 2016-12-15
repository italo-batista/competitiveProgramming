# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

q = int(raw_input())

for i in range(q):

	errado = str(raw_input())
	mid = len(errado) / 2
	
	certo = ""
	for j in range(mid-1, -1, -1):
		certo += errado[j]
	for j in range(len(errado)-1, mid-1, -1):
		certo += errado[j]
	print certo
	
