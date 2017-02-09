import Queue

# LINK FOR PROBLEM: http://codeforces.com/problemset/problem/520/B


# SOLUÇÃO ITERATIVA

def isEven(number):
    return (number % 2 == 0)

n, m = map(int, raw_input().split())
ops = 0
copy_m = m

while copy_m != n:

    if copy_m < n:
        copy_m = copy_m + 1
        ops += 1

    else:

        if isEven(copy_m):
            copy_m = copy_m / 2
            ops += 1

        else:
            copy_m = copy_m + 1
            copy_m = copy_m / 2
            ops += 2

print ops



# SOLUÇÃO POR GRAFO E BSF

graph = [[0, 0]]
graph.extend([[i-1, i*2] for i in range(1, 10001)])

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

n, m = map(int, raw_input().split())
print bfs(n, m)
