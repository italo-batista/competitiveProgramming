#coding: utf-8

def compression(string):

	tam = len(string)
	compressed = []
	last_letter = string[0]
	count_last_letter = 1

	for i in range(1, tam):
		if last_letter == string[i]:
			count_last_letter += 1
		else:
			compressed.append(last_letter + str(count_last_letter))
			last_letter = string[i]
			count_last_letter = 1

	compressed.append(last_letter + str(count_last_letter))
	new_string = ''.join(compressed)

	return string if len(new_string) == tam else new_string

assert compression('aabccccaa') == 'a2b1c3a2'
assert compression('aabbcc') == 'aabbcc'
assert compression('aabbbcc') == 'a2b3c2'
