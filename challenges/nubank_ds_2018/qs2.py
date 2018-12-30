global XPEER_INDEX, CATEGORY_INDEX, HAND_TIME_INDEX
XPEER_INDEX, CATEGORY_INDEX, HAND_TIME_INDEX = 0, 1, 2

def get_xpeers_ids(data):
	return list(set([row[XPEER_INDEX] for row in data]))

def get_categories(data):
	return list(set([row[CATEGORY_INDEX] for row in data]))

def get_handling_time(data):
	return list(set([row[HAND_TIME_INDEX] for row in data]))

def _by_category(row, cat_id):
	return row[CATEGORY_INDEX] == cat_id

def _by_xpeer_id(row, xpeer_id):
	return row[XPEER_INDEX] == xpeer_id

def calc_avg(nums):
	return sum(nums) / len(nums)

def print_output(output):
	for row in output:
		print " ".join(row)
	
def calculate_aht(data):
	
	def __calculate_aht(data, cat_id):
		filtered_by_cat = filter(
			lambda row: _by_category(row, cat_id), data)
		times = get_handling_time(filtered_by_cat)
		avg_time = calc_avg(times)
		return avg_time
				
	output = []
	xpeers_ids = get_xpeers_ids(data)
	xpeers_ids.sort()
	
	for xid in xpeers_ids:		
		xpeer_rows = filter(lambda row: _by_xpeer_id(row, xid), data)
		m_xpeer_cats = get_categories(xpeer_rows)
		m_xpeer_cats.sort()
				
		for category_id in m_xpeer_cats:
			aht = __calculate_aht(xpeer_rows, category_id)			
			output.append([str(xid), str(category_id), str(aht)])
	
	return output

if __name__ == "__main__":
	
	matrix = []
	
	try:
		while True:			
			new_row = map(int, raw_input().split())
			matrix.append(new_row)
			
	except EOFError:
		output = calculate_aht(matrix)
		print_output(output)
