def calc_median(nums, n):
	nums.sort()
	i = n / 2 
	
	if n % 2 != 0:
		median = nums[i]
	else:
		median = (nums[i-1] + nums[i]) / 2.0
	
	return median
	
def quartiles(nums, n):
	nums.sort()	
	median = calc_median(nums, n)
		
	if n % 2 == 0: #even
		center_i = n / 2
		lower_half = nums[:center_i]
		upper_half = nums[center_i:]
	else:
		center_i = (n - 1) / 2 
		lower_half = nums[:center_i]
		upper_half = nums[center_i+1:]
	
	q1 = calc_median(lower_half, len(lower_half))
	q2 = median
	q3 = calc_median(upper_half, len(upper_half))
	
	return (q1, q2, q3)
	

if __name__ == "__main__":
	n = int(raw_input())
	nums = map(int, raw_input().split())
	q1, q2, q3 = quartiles(nums, n)
	print(q1)
	print(q2)
	print(q3)
