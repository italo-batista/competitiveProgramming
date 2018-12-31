import math

def m_sum(nums):
	return reduce(lambda x,y: x + y, nums)

def mean(nums):
	return m_sum(nums) * 1.0 / len(nums)

def square_dist(x, u):
	"""Args: :int: x, num.
			 :int: u, mean."""
	return (x - u) ** 2
	
def stand_deviation(nums, n):
	u = mean(nums)	
	square_dists = [square_dist(x, u) for x in nums]
		
	return math.sqrt(mean(square_dists))

def print_round(n):
	print "{0:.1f}".format(round(n, 1)) 


if __name__ == "__main__":
	n = int(raw_input())
	nums = map(int, raw_input().split())	
	
	print_round(stand_deviation(nums, n))
