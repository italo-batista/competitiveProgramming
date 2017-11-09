#coding: utf-8

def urlify(string, tam):

	i = tam - 1
	j = len(string)
	count_spaces = 0

	while i - count_spaces >= 0:
		if string[i] == " ":
			string = string[:j-3] + "%20" + string[j:]
			count_spaces += 1
			j -= 3
		else:
			string = string[:j-1] + string[i] + string[j:]
			j -= 1
		i -= 1		
	
	return string

print urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
