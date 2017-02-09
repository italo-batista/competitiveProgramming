import Queue

# INSTANCIE GRAPH COMO SEU GRAFO (LISTA OU MATRIZ DE ADJ)
graph = []

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

        for adjacent in graph[top]:

            if not visited[adjacent]:
                distances[adjacent] = distances[top] + 1
                visited[adjacent] = True
                queue.put(adjacent)

                if adjacent == target:
                    return distances[adjacent]