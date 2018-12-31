from itertools import groupby
from operator import itemgetter

n = int(raw_input())
nums = map(int, raw_input().split())

def m_sum(nums):
	return reduce(lambda x,y: x + y, nums)

def mean(nums, n):
	return m_sum(nums) / 1.0 / n
	
def median(nums, n):
	nums.sort()
	i = n / 2 
		
	if n % 2 != 0:
		median = nums[i]
	else:
		median = (nums[i-1] + nums[i]) / 2.0
	
	return median

def mode(nums):
	nums.sort()
	temp = [(key, len(list(group))) for key, group in groupby(nums)]
	mode = max(temp, key=itemgetter(1))
	return mode[0]
		
print mean(nums, n)
print median(nums, n)
print mode(nums)
