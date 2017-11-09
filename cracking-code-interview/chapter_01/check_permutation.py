import string

def check_permutation(str1, str2):
	
	if len(str1) != len(str2):
		return False
	
	tam = len(str1)
letters = dict((letter, 0) for letter in set(str1))          # hash table

	for i in xrange(tam):		
		l1 = str1[i]
		letters[l1] = letters[l1] + 1
		l2 = str2[i]
		letters[l2] = letters[l2] - 1

	if letters.values().count(0) == 26:
		return True
	
	return False

assert check_permutation('aba', 'abb') == True
