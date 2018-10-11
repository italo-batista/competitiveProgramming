def is_valid(code):
	code = int(code)
	if code in range(65, 90 + 1) \
		or code in range(97, 122 + 1) \
		or code == 32:
		return True
	return False
	
def convert_code_list_to_str(code_list):
	return ''.join(chr(code) for code in code_list)	

def get_code_substring(i, shift, reversed_code, valid_code_list):
	code_substring = int(reversed_code[i:i+shift])
	valid_code_list.append(code_substring)	

def decode(encoded):
	reversed_code = encoded[::-1]
	valid_code_list = []
		
	i = 0
	str_len = len(reversed_code)
	while i < str_len:
			
		if is_valid(reversed_code[i:i+2]):								
			shift = 2
			get_code_substring(i, shift, reversed_code, valid_code_list)
		
		elif is_valid(reversed_code[i:i+3]):
			shift = 3
			get_code_substring(i, shift, reversed_code, valid_code_list)
		
		else:
			shift = 1
		
		i = i + shift

	decoded_str = convert_code_list_to_str(valid_code_list)
	return decoded_str

