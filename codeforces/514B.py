import math
	
def isColinear(s1, s2):
	
	x1 = x
	y1 = y
	x2 = s1[0]
	y2 = s1[1]
	x3 = s2[0]
	y3 = s2[1]
	
	return ((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) == 0) or (x1 == x2 == x3) or (y1 == y2 == y3)

n, x, y = map(int, raw_input().split())

soldiers = []

for i in range(n):
	x1, y1 = map(int, raw_input().split())
	s = (x1, y1)
	soldiers.append(s)

ans = 0
while len(soldiers) > 0:
	
	temp = []
	for j in range(len(soldiers)):
		if j != 0 and not isColinear(soldiers[0], soldiers[j]):
			temp.append(soldiers[j])

	ans += 1
	soldiers = temp
		
print ans
