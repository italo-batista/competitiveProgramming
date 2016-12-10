# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/430/B

ent = map(int, raw_input().split())
n = ent[0]
k = ent[1]
x = ent[2]
balls = map(int, raw_input().split())

indexs = []
res = 0

for i in range(0,len(balls) - 1):

	if balls[i] == x and balls[i + 1] == x:

		temp = i
		indexs.append(temp)
		temp = i + 1
		indexs.append(temp)

for i in range(0, len(indexs), 2):
	temp_balls = balls[:]
	
	del temp_balls[indexs[i]]
	del temp_balls[indexs[i]]
	
	# remove possible balls to be removed given ball inserted way by player
	j = 0
	count = 0
	while len(temp_balls) > 0 and j < len(temp_balls) - 2:
		if temp_balls[j] == temp_balls[j + 1] and temp_balls[j] == temp_balls[j + 2]:
			color = temp_balls[j]
			while len(temp_balls) > 0 and j < len(temp_balls) and temp_balls[j] == color:
				temp_balls.pop(j)
				count += 1
			j = 0
		else:
			j += 1
	
	temp = count
	
	
	if temp > res:
		res = temp

if len(indexs) > 0:
	res += 2

if len(balls) <= 1:
	res = 0
	
print res
