
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




# OLD SOLUTION

#while True:

	#try:
		#n = int(raw_input())
		#despesa = input()

		#lucros = [0] * (n+1)
		#for i in xrange(1, n+1, 1):
			#c = input()
			#lucros[i] = c

		#dp = []
		#for i in xrange(n+1):
			#array = []
			#for j in xrange(n+1):
				#array.append(0)
			#dp.append(array)
		
		#maiorLucro = (0,0)
		#for i in xrange(1, n+1, 1):
			#for j in range(i, n+1, 1):
				
				#lucroPassado = dp[i][j-1]
				#lucroAtual = lucroPassado + lucros[j] - despesa
								
				#atualMaiorLucro = dp[maiorLucro[0]][maiorLucro[1]]				
				#if lucroAtual > atualMaiorLucro:
					#maiorLucro = (i, j)
					
				#dp[i][j] = max([lucroAtual, 0])
															
		#print atualMaiorLucro

	#except: break
