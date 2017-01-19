
m = []

for i in range(4):
	row = map(str, raw_input().split())
	m.append(row)

YES = False


# horizontal
for row in m:
	if ".xx" in row[0] or "x.x" in row[0] or "xx." in row[0] or "xxx" in row[0]:
		YES = True
		
# vertical
for x in range(4):
	column = "".join([ m[0][0][x], m[1][0][x], m[2][0][x], m[3][0][x] ] )
	if ".xx" in column or "x.x" in column or "xx." in column or "xxx" in column:
		YES = True
		
# diagonal

diag = "".join([ m[0][0][0], m[1][0][1], m[2][0][2] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True

diag = "".join([ m[0][0][1], m[1][0][2], m[2][0][3] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True

diag = "".join([ m[1][0][0], m[2][0][1], m[3][0][2] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True

diag = "".join([ m[1][0][1], m[2][0][2], m[3][0][3] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True

for i in range(2):
	diag = "".join([ m[i][0][3-i], m[1+i][0][3-1-i], m[2+i][0][3-2-i] ] )
	if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
		YES = True
	
diag = "".join([ m[0][0][2], m[1][0][1], m[2][0][0] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True
	
diag = "".join([ m[1][0][3], m[2][0][2], m[3][0][1] ] )
if ".xx" == diag or "x.x" == diag or "xx." == diag or "xxx" == diag:
	YES = True
	
if YES:
	print "YES"
else:
	print "NO"
