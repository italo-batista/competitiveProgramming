import Queue

pontos, ligs = map(int, raw_input().split())


# MONTA MAPA

mapl = {}
entradas = []

count = 0
for i in range(ligs):

    pi, pii = map(str, raw_input().split())

    entradas.append((pi, pii))

    if pi not in mapl:
        mapl[pi] = count
        count += 1

    if pii not in mapl:
        mapl[pii] = count
        count += 1


# MONTA GRAFO

grafo = [[] for i in range(pontos)]

for pi, pii in entradas:

        p1 = mapl[pi]
        p2 = mapl[pii]
        grafo[p1].append(p2)
        grafo[p2].append(p1)


# LOGICA

def bfs(start, target):

    LIMIT = 20001

    queue = Queue.Queue()
    distances = [float('inf')] * LIMIT
    visited = [False] * LIMIT

    queue.put(start)
    visited[start] = True
    distances[start] = 0

    while not queue.empty():

        top = queue.get()

        for adjacent in grafo[top]:

            if not visited[adjacent]:
                distances[adjacent] = distances[top] + 1
                visited[adjacent] = True
                queue.put(adjacent)

                if adjacent == target:
                    return distances[adjacent]

distancia = bfs(mapl["Entrada"], mapl["*"]) + bfs(mapl["*"], mapl["Saida"])
print distancia