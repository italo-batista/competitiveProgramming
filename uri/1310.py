
while True:

	try:
		n = int(raw_input())
		despesaFixa = input()
		
		maiorLucro = 0
		lucroAcumulado = 0

		for i in xrange(n):
			
			lucroDoDia = input()
			lucroAcumulado = lucroAcumulado + lucroDoDia - despesaFixa
			maiorLucro = max([maiorLucro, lucroAcumulado])
			
			if lucroAcumulado < 0:
				lucroAcumulado = 0
														
		print maiorLucro

	except: break


