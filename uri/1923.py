import Queue

n, g = map(int, raw_input().split())


# MONTA ESTRUTURAS

LIMIT = n * g + 10
mapl = {}
mapl_reversed = {}
entries = []
invited = []
distances = [float('inf')] * LIMIT
visited = [False] * LIMIT

count = 0
for i in range(n):

	person1, person2 = map(str, raw_input().split())

	entries.append((person1, person2))

	if person1 not in mapl:
		mapl[person1] = count
		mapl_reversed[count] = person1
		count += 1
		
	if person2 not in mapl:
		mapl[person2] = count
		mapl_reversed[count] = person2
		count += 1


# MONTA GRAFO

grafo = [[] for i in range(n)]

for person1, person2 in entries:

	p1_index = mapl[person1]
	p2_index = mapl[person2]
	grafo[p1_index].append(p2_index)
	grafo[p2_index].append(p1_index)

# LOGICA

def bfs(start, dist_max):

	queue = Queue.Queue()

	queue.put(start)
	visited[start] = True
	distances[start] = 0

	while not queue.empty():

		top = queue.get()

		for adjacent in grafo[top]:

			# se a distancia do atual ponto for maior do que o grau max de relacionamento
			if distances[top] + 1 > dist_max:
				return False

			if not visited[adjacent]:
				distances[adjacent] = distances[top] + 1
				visited[adjacent] = True
				
				# get invited's name by his index (adjacent)
				person = mapl_reversed[adjacent]
				invited.append(person)
				
				queue.put(adjacent)
				

rerisson_index = mapl["Rerisson"]
bfs(rerisson_index, g)

invited.sort()
print len(invited)
for person in invited:
	print person

