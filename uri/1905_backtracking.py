def validate(row, col):
    if col > 4 or col < 0 or row > 4 or row < 0 or lab[row][col] == "1" or visited[row][col]:
	return False 
    return True

def backtracking(row, col):
    
    visited[row][col] = True
    
    if (row == 4 and col == 4):
	    return True
	    
    else:

	if validate(row, col+1) and backtracking(row, col+1):
	    return True
	if validate(row, col-1) and backtracking(row, col-1):
	    return True
	if validate(row+1, col) and backtracking(row+1, col):
	    return True
	if validate(row-1, col) and backtracking(row-1, col):
	    return True
	
    return False


t = int(raw_input())

for i in range(t):

    lab = []
    visited = []
    
    count = 0
    while count < 5:

        new_row = str(raw_input()).split()
        if len(new_row) > 0:
            count = count + 1
            lab.append(new_row)
	    visited.append([False]*5)
                      
    if backtracking(0, 0):
        print "COPS"
    else:
        print "ROBBERS"
