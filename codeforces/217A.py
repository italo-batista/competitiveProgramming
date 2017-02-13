def dfs(myPoint):
    visited.append(myPoint)
    not_visited = [x for x in graph if x not in visited]

    for point in not_visited:
        if point[0] == myPoint[0] or point[1] == myPoint[1]:
                dfs(point)


# FLOW STARTS HERE

n = input()
graph = []
visited = []
n_componentes = 0

for i in xrange(n):
    i, j = map(int, raw_input().split())
    graph.append((i, j))

for point in graph:
    if point not in visited:
        dfs(point)
        n_componentes += 1

print n_componentes - 1
