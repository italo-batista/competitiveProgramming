# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/722/A


tipo = int(raw_input())
ent = map(str, raw_input().split(":"))
hh = ent[0]
mm = ent[1]


if (tipo == 24):
			
	if (int(hh) > 23):
		
		if (int(hh[0]) > 2):
			hh = "0" + str(hh[1])
		elif (int(hh[1]) > 3):
			hh = str(hh[0]) + "0"

	
elif (tipo == 12):
	
	if (int(hh) > 12):
		
		if (int(hh[0]) > 1):
			if (int(hh[1]) == 0):
				hh = "1" + str(hh[1])
			else:
				hh = "0" + str(hh[1])
				
		elif (int(hh[1]) > 2):
			hh = str(hh[0]) + "0"
	
	if (int(hh) == 00):
		hh = "01"
	

if (int(mm) >= 60):
	if (int(mm[0]) > 5):
		mm = "0"  + str(mm[1])
	
print hh+":"+mm
