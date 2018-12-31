n = int(raw_input())
nums = map(int, raw_input().split())
wheights = map(int, raw_input().split())

def m_sum(nums):
	return reduce(lambda x,y: x + y, nums)

def wheighted_mean(nums, n):
	def wheighted_sum(x, y):
		if type(x) == tuple:
			return (x[0] * x[1]) + (y[0] * y[1])
		else:
			return x + (y[0] * y[1])
	
	m_wheighted_sum = reduce(wheighted_sum, zip(nums, wheights))
	return  float(m_wheighted_sum) / float(m_sum(wheights))

print "{0:.1f}".format(round(wheighted_mean(nums, wheights), 1)) 
