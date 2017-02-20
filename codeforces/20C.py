import Queue

n, m = map(int, raw_input().split())
LIMIT = 110010


# MONTA ESTRUTURAS

distances = [float('inf')] * LIMIT
pares = [float('inf')] * LIMIT

grafo = [0] * LIMIT
for i in range(LIMIT): grafo[i] = []

for i in range(m):
        x, y, p = map(int, raw_input().split())
        grafo[x].append((y, p))
        grafo[y].append((x, p))


# DJKISTRA ALGO

def dijkstra():

    FIRST = 0
    SECOND = 1

    distances[1] = 0
    queue = Queue.PriorityQueue()
    queue.put((0, 1))

    while not queue.empty():

        last_out = queue.get()

        top = last_out[SECOND]
        dist = last_out[FIRST]

        if dist == distances[top]:

            for adj in grafo[top]:

                no = adj[FIRST]
                peso = adj[SECOND]

                if distances[no] == -1 or distances[no] > dist + peso:
                    distances[no] = dist + peso
                    pair = (distances[no], no)
                    queue.put(pair)

                    pares[no] = top


# LOGICA
djkistra()

if distances[n] == float('inf'):
    print -1

else:
    t = n
    ans = []
    while t != 1:
        ans.append(t)
        t = pares[t]

    print "1 " + " ".join(str(x) for x in reversed(ans))





