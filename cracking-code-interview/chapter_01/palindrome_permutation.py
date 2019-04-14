#coding: utf-8


""" To be more precise, strings with even length (after removing all non-letter characters) must
have all even counts of characters. Strings of an odd length must have exactly one character with
an odd count. Of course, an "even" string can't have an odd number of exactly one character,
otherwise it wouldn't be an even-length string (an odd number+ many even numbers= an odd number).
Likewise, a string with odd length can't have all characters with even counts (sum of evens is
even). It's therefore sufficient to say that, to be a permutation ot a palindrome, a string can
have no more than one character that is odd. This will cover both the odd and the even cases."""


def palindrome_permutation_bitwise(string):
	string = string.lower()
	checker = 0
	A_ASCII = 97

	for c in string:
		char_code = ord(c) - A_ASCII

		if (checker & (1 << char_code)) > 0:  # char already in check
			checker &= ~(1 << char_code)  # dismark char code
		else:
			checker |= (1 << char_code)  # mark char code

	has_odd_lenght = len(string) % 2 != 0
	if has_odd_lenght:
		return (checker & (checker -1)) == 0
	else:
		return checker == 0



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


assert palindrome_permutation("tactcoapapa") == True
assert palindrome_permutation("italoolati") == True
assert palindrome_permutation("italomolati") == True
assert palindrome_permutation("italoxyzolati") == False

assert palindrome_permutation_bitwise("tactcoapapa") == True
assert palindrome_permutation_bitwise("italoolati") == True
assert palindrome_permutation_bitwise("italomolati") == True
assert palindrome_permutation_bitwise("italoxyzolati") == False
