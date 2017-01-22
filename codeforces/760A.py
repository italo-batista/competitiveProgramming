meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a, b = map(int, raw_input().split())

c = meses[a] - (8 - b)

#print c

t = 1
t += c / 7

#print t

c = c % 7

#print c

if c > 0:
	t += 1
	
print t
