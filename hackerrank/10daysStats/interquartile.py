from quartiles import quartiles

def diff_interquartiile(nums):
	q1, q2, q3 = map(float, quartiles(nums, len(nums)))
	print q3 - q1
	
if __name__ == "__main__":
	n = int(raw_input())
	xs = map(int, raw_input().split())
	fs = map(int, raw_input().split())
	
	nums = []
	for x,f in zip(xs, fs):
		nums = nums + ([x] * f)
	
	diff_interquartiile(nums)

	
