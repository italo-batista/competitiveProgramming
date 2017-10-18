
def marcou_mais_de_uma(valores):
	
	n = len(filter(lambda x: x <= 127, valores))
	
	if n > 1:
		return True
	
	return False

def marcou_nenhuma(valores):
	
	n = len(filter(lambda x: x > 127, valores))
	
	if n == 5:
		return True
	
	return False

while True:
	
	n = input()
	
	if n == 0: break

	for i in range(n):
		a, b, c, d, e = map(int, raw_input().split())
		opts = [a, b, c, d, e]
		
		if marcou_mais_de_uma(opts):
			print "*"
		
		elif marcou_nenhuma(opts):
			print "*"
		
		else:
			
			for j in range(5):
				if opts[j] <= 127:
					print chr(65 + j)
		

