# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/731/A

def findHorario(ci, letter):	
	p = 0
	j = ci
	while (j != j-1):
		
		if (letter == alfab[j]):
			break
		
		if (j == len(alfab)-1):
			j = 0
		else:
			j = j + 1
		
		p = p + 1
	
	return p
		
		
def findAntihorario(ci, letter):
	p = 0
	j = ci
	while (j != j+1):
		
		if (letter == alfab[j]):
			break

		if (j == 0):
			j = len(alfab) - 1
		else:
			j = j - 1
		
		p = p + 1

	return p


alfab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

word = str(raw_input())

passos = 0
current = 0
for i in range(len(word)):

	letter = word[i]
	
	passos_h = findHorario(current, letter)
	passos_ant_h = findAntihorario(current, letter)
		
	if (passos_h <= passos_ant_h):
		passos = passos + passos_h
	else:
		passos = passos + passos_ant_h

	current = alfab.index(letter)

print passos
