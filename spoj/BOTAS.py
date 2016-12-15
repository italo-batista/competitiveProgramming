# LINK FOR PROBLEM: http://br.spoj.com/problems/BOTAS/


while True:
	
	try:
		n = int(raw_input())
		botasd = [0] * 61
		botase = [0] * 61
		
		for i in range(n):
			
			m, l =  map(str, raw_input().split())
			m = int(m)
			if l == "D":
				botasd[m] += 1
			else:
				botase[m] += 1
		
		pares = 0
		for i in range(30, 61):
			if botasd[i] >= botase[i]:
				pares += botase[i]
			else:
				pares += botasd[i]
		print pares
				
	except:
		break
