#coding: utf-8

def palindrome_permutation(string):

	string = string.lower()
	chars = dict((letter, 0) for letter in set(string)) 

	for c in string:
		chars[c] = chars[c] + 1
	
	if " " in chars.values():
		chars.pop(" ")	

	has_value_one = False
	for k, v in chars.items():

		if has_value_one and v == 1:
			return False
		elif v == 1:
			has_value_one = True

		if has_value_one  and v != 2:
			return False
		
		return True


print palindrome_permutation("tactcoapapa") == True
