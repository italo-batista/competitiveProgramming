
def f(coefs, positions):	
	place = reduce(
		lambda v, pair: (v[0]*v[1] + pair[0]*pair[1], 1),  
		zip(coefs, positions)
	)
	return place[0]

while True:
	
	try:

		n_contests, n_students = map(int, raw_input().split())
		coefs = map(int, raw_input().split())
		classifications = dict()
		valid = True
		
		if (n_contests == 2):
			
			for i in range(n_students):
				for j in range(n_students):
					
					positions = [i, j]
					place = f(coefs, positions)
					
					if classifications.has_key(place):
						valid = False
					else:
						classifications[place] = True			
			
			
		elif (n_contests == 3):
			
			for i in range(n_students):
				for j in range(n_students):
					for k in range(n_students):
						
						positions = [i, j, k]
						place = f(coefs, positions)
						
						if classifications.has_key(place):
							valid = False
						else:
							classifications[place] = True
					
		if valid:
			print "Lucky Denis!"
		else:
			print "Try again later, Denis..."
		
	
	except Exception:
		break
