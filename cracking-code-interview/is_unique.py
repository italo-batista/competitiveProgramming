

def is_unique(string):  
  
  A_ASCII = 97
  checker = 0
  
  for i in xrange(len(string)):    
    value = ord(string[i].lowert()) - A_ASCII	
    if (checker & (1 << value)) > 0:		        # Bitwise AND to check if value is already set on checker 
	return False				                                 	
    checker |= (1 << value)				# Turns 1 the position of current char (LSB: ‘a’, MSB:’z’) to say 
							# that the char is already used.  

								                                      
string = input()
is_unique(string)
