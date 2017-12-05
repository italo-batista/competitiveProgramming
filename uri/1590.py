# coding:utf-8

def backtracking(curr_sum, curr_k, k):
	
	global larger_sum
	
	for i, num in enumerate(nums):
				
		if curr_k == 0:
			curr_sum = num
		
		if i not in select:

			select[curr_k] = i			
			m_sum = curr_sum & num
							
			if curr_k + 1 >= k and m_sum > larger_sum:
				larger_sum = m_sum
			
			elif m_sum > larger_sum:
				backtracking(m_sum, curr_k + 1, k)
			
		
t = input()
for teste in range(t):
	
	n, k = map(int, raw_input().split())
	nums = map(int, raw_input().split())
	
	nums.sort(reverse=True)
	select = [-1 for i in range(n)]
	
	larger_sum = 0
	backtracking(0, 0, k)
	print larger_sum
