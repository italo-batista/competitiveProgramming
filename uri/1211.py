
def is_ok(numbers, ok):
    
    if ok[0]:
	if numbers[0] == numbers[1]:
	    return True
	else:
	    ok[0] = False
    return False

while True:
    
    try:
        
        n = int(raw_input())
        tels = []
        
        for i in xrange(n):	    
	    tel = str(raw_input())
	    tels.append(tel)			
	tels.sort()

	not_done = True
	economies = []
	i, j = 0, 1
	equals = 0

	while not_done:
			
	    if n <= 1:
		not_done = False
		break
			
	    ok = [True]
	    m_equals = len(filter(lambda x: is_ok(x, ok) and x[0] == x[1], zip(tels[i], tels[j])))
			
	    if m_equals == 0:
		economies.append(equals)
		equals = 0
	    else:
		equals += m_equals
			
	    if j == n - 1:
		not_done = False
	    else:
		i += 1
		j += 1
				
	economies.append(equals)
	print sum(economies)
							                    
    except EOFError:
        break


