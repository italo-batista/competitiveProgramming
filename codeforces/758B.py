
# LINK FOR THE PROBLEM: http://codeforces.com/contest/758/problem/B

s = str(raw_input())

sr, sb, sg, sy = 0, 0, 0, 0
tr, tb, tg, ty = False, False, False, False
for i in range(len(s)):
	
	if tr and tb and tg and ty:
		break
		
	if not tr and s[i] == "R":
		sr = i % 4
		tr = True
		
	if not tb and s[i] == "B":
		sb = i % 4
		tb = True

	if not tg and s[i] == "G":
		sg = i % 4
		tg = True

	if not ty and s[i] == "Y":
		sy = i % 4
		ty = True		

kr, kb, kg, ky = 0, 0, 0, 0
for i in range(sr, len(s), 4):
	if s[i] == "!":	kr += 1

for i in range(sb, len(s), 4):
	if s[i] == "!":	kb += 1

for i in range(sg, len(s), 4):
	if s[i] == "!":	kg += 1

for i in range(sy, len(s), 4):
	if s[i] == "!":	ky += 1
		
print kr, kb, ky, kg
