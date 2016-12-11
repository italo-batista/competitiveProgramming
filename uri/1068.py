# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1068

import math

while True:
	
	try:
		exp = str(raw_input())
		
		isCorrect = True
		pilha = []

		
		for i in range(len(exp)):
			
			if exp[i] == "(":
				pilha.append(exp[i])
			
			if exp[i] == ")":
				
				if  len(pilha) > 0:
					pilha.pop()	
				
				else:
					isCorrect = False
					break
					
		if isCorrect and len(pilha) == 0:
			print "correct"
		else:
			print "incorrect"
			
						
	except:
		break
