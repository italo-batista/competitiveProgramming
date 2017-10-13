import math

def is_on_same_board_house(x1, y1, x2, y2):
	return x2 == x1 and y2 == y1

def is_same_diag(x1, y1, x2, y2):
	return abs(x2 - x1) == abs(y2 - y1)

def is_same_row(x1, x2):
	return x2 == x1
	
def is_same_col(y1, y2):
	return y2 == y1

entrada = raw_input()

while entrada != "0 0 0 0":
	x1, y1, x2, y2 = map(int, entrada.split())
	
	if is_on_same_board_house(x1, y1, x2, y2):
		print 0
		
	elif is_same_diag(x1, y1, x2, y2):
		print 1
	
	elif is_same_row(x1, x2):
		print 1
		
	elif is_same_col(y1, y2):
		print 1
	
	else:
		print 2
		
	entrada = raw_input()
	
	
