import Queue as qq

def bfs(start, target):

    LIMIT = 5000000
    distances = [float('inf')] * LIMIT
    visited = [False] * LIMIT

    queue = qq.Queue()
    queue.put(start)
    visited[start] = True
    distances[start] = 0

    while not queue.empty():
        top = queue.get()

        for adjacent in xrange(len(matriz[top])):

            if matriz[top][adjacent] != target and not visited[adjacent]:
                distances[adjacent] = distances[top] + 1
                visited[adjacent] = True
                queue.put(adjacent)


    return distances[n - 1]


n, m = map(int, raw_input().split())
matriz = [[1 for i in xrange(n)] for j in xrange(n)]

for x in xrange(m):

    i, j = map(int, raw_input().split())
    i -= 1
    j -= 1
    matriz[i][j] = 2
    matriz[j][i] = 2


res = bfs(0, matriz[0][n - 1])
if res == float('inf'):
    print -1
else:
    print res