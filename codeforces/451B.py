# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/451/B

n = int(raw_input())
ent = map(int, raw_input().split())

change = []
changed = False

for i in range(n-1):
	
	if ent[i] > ent[i+1] and not changed:
		changed = True
		change.append(i)
	
	if changed:
		if ent[i] < ent[i+1]:
			changed = False
			change.append(i)



# o array estah totalmente ordenado
if len(change) == 0:
	print "yes\n1 1"

# o array estah totalmente revertido
elif len(change) == 1 and change[0] == 0:
	change.append(n-1)
	print "yes"
	print change[0]+1, change[1]+1

# tem mais de um segmento revertido
elif len(change) > 2:
	print "no"
	
else:

	flag = False

	# swap
	if len(change) == 1:
		change.append(n-1)

	t = ent[ change[0] ]
	ent[ change[0] ] = ent[ change[1] ]
	ent[ change[1] ] = t
		
	# descobrindo se ha falhas
	for j in range(change[0]):

		if ent[j] > ent[j+1]:
			flag = True
			break
			
	# descobrindo se ha falhas			
	for j in range(change[1], n-1, 1):
		
		if ent[j] > ent[j+1]:
			flag = True
			break

	if flag:
		print "no"
	else:
		print "yes"
		print change[0]+1, change[1]+1
