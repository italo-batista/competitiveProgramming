
while True:
	
	h1, m1, h2, m2 = map(int, raw_input().split())
	
	if h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0:
		break
	
	if h1 == h2:
		if m1 < m2:
			print m2 - m1
		elif m1 > m2:
			print 24 * 60 - (m1 - m2)
		else:
			print 0
	
	elif h1 < h2:
		print (h2 - h1) * 60 - m1 + m2
	
	else:
		print (24 - h1) * 60 - m1 + (h2 * 60) + m2
	
