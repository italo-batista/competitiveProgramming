# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/501/B


q = int(raw_input())

handles = dict()

for i in range(q):
	
	old, new = map(str, raw_input().split())
		
	# primeira vez que o user muda de nome
	if not handles.has_key(old):
		handles[new] = old
	
	
	if not handles.has_key(new):
			
			if handles.has_key(old):
				
				firstHandle = handles[old]
				handles.pop(old)
				handles[new] = firstHandle
	

iterator = handles.iteritems()
handle = iterator.next()

print len(handles)
while (handle != ""):
	print handle[1],handle[0]
	try:
		handle = iterator.next()
	except:
		break
		

		
		
	
	


