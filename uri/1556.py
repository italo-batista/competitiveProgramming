while True:
	try:
		sequence = str(raw_input())
		substrings = dict()

		def remove_letters(sequence):
				
			substrings[sequence] = True	
			for i in range(len(sequence)):
								
					m_sequence = sequence[:i] + sequence[i+1:]					
				
					try:
						substrings[m_sequence]
				
					except Exception:					
						substrings[m_sequence] = True					
						remove_letters(m_sequence)
						
		remove_letters(sequence)

		for s in sorted(substrings):
				if s != "":
					print s

		print ""
	
	except Exception:
		break
