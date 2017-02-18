import Queue

grafo = []

def djkistra(start, target):

    LIMIT = 20001
    NO = 1
    Y = 0
    PESO = 1
    DIST = 1

    queue = Queue.PriorityQueue()
    distances = [float('inf')] * LIMIT
    visited = [False] * LIMIT

    queue.put(start)
    visited[start] = True
    distances[start] = 0

    while not queue.empty():

        top = queue.get()

        # top: (dist, (y, peso))

        for adj in grafo[top[NO][Y]]:

            if not visited[adj[Y]]:
                distances[adj[Y]] = distances[top[DIST]] + top[NO][PESO]
                visited[adj[Y]] = True
                queue.put( (distances[adj[Y]], adj) )

                if adj[Y] == target:
                    return distances[adj[Y]]