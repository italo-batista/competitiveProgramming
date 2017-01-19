
n = int(raw_input())
a = map(int, raw_input().split())
r = []
compare = [0] * n



if a == compare:
	print "NO"

else:
	
	print "YES"
	
	if a[-1] == 0:
			
			temp = ()
			j = n-1
			mysum = 0
			while mysum == 0:
				j = j - 1
				mysum += a[j]

			if sum(a[0:j]) == 0:
				temp = (0, n-1)
				j = 0
			else:
				temp = (j, n-1)
				
			i = 0
			while i < j:
				
				if a[i] == 0:
					j = i
					mysum = 0
					while mysum == 0:
						j = j + 1
						mysum += a[j]
					r.append( (i, j) )
					i = j
				else:			
					r.append( (i, i) )
				
				i = i + 1
				
			r.append(temp)
	else:
		
			i = 0
			while i < n:
				
				if a[i] == 0:
					j = i
					mysum = 0
					while mysum == 0:
						j = j + 1
						mysum += a[j]
					r.append( (i, j) )
					i = j
				else:			
					r.append( (i, i) )
				
				i = i + 1
	
	print len(r)
	
	for tupla in r:
		print tupla[0]+1, tupla[1]+1
					
	



