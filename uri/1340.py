# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/pt/problems/view/1340

import Queue

while True:
	
	try:
	
			n = int(raw_input())
			
			fila  = Queue.Queue()
			pilha = Queue.LifoQueue()
			prior = Queue.PriorityQueue()
			
			isQueue = True
			isStack = True
			isPriory = True
			notSure = True
			
			for i in range(n):
				op, x = map(int, raw_input().split())
				
				if op == 1:
					fila.put(x)
					pilha.put(x)
					prior.put(100-x)
					
				else:
					
					filaGet = fila.get()
					pilhaGet = pilha.get()
					priorGet = prior.get()
					
											
					if x != filaGet:
						isQueue = False
	
					if x != pilhaGet:
						isStack = False
						
					if (100-x) != priorGet:
						isPriory = False
				
			
			if not isPriory and not isQueue and not isStack:
				print "impossible"
			elif isQueue and not isPriory and not isStack:
				print "queue"
			elif isStack and not isQueue and not isPriory:
				print "stack"
			elif isPriory and not isStack and not isQueue:
				print "priority queue"
			else:
				print "not sure"
	
	
	except:
		break

