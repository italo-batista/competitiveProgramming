# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/625/B

marca = str(raw_input())
plagio = str(raw_input())

cont = 0
i = 0
while (i < len(marca) - len(plagio) + 1):
	
	flag = True	
	if (marca[i] == plagio[0]):
		
		teste = True
		for j in range(len(plagio)):
			
			if (marca[j+i] != plagio[j]):
				teste = False
				break

		if (teste):
			cont = cont + 1
			i = i + len(plagio)
			flag = False

	if (flag):
		i = i + 1
	
print cont
