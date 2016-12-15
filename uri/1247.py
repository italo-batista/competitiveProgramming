import math
# LINK FOR PROBLEM: https://www.urionlinejudge.com.br/judge/en/problems/view/1247

while True:
	
	try:
		d, vf, vg =  map(int, raw_input().split())
		
		s1 = 12.0
		s2 = math.sqrt( d*d + 12*12)
		
		t1 = s1 / vf
		t2 = s2 / vg
			
		if t1 >= t2:
			print "S"
		else:
			print "N"
		
	except:
		break
