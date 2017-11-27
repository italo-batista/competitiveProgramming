import sys

sys.setrecursionlimit(20000)

ans = []
cod = ['N', 'O', 'P']

def validate(seg):
	
	for i in range(1, len(seg)):
	
		start_i = len(seg) - i - i
		start_j = len(seg) - i	
		
		equal = True
		for k in range(i):
			if seg[start_i] != seg[start_j]:
				equal = False
				break
			start_i += 1
			start_j += 1
		
		if equal:
			return False
		
	return True
	

def backtracking(sequence):
		
	if len(sequence) >= 5000:
		print sequence
		return True
	
	else:
		
		for letter in cod:
			
			valid = validate(sequence + letter)
			
			if valid and backtracking(sequence + letter):
				return True
				
	return False
				
backtracking("N")
