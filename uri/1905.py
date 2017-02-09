
def dfs(row, col):
    visited[row][col] = True

    if col < 4 and not visited[row][col+1] and graph[row][col+1] == "0":
        dfs(row, col+1)

    if col > 0 and not visited[row][col-1] and graph[row][col-1] == "0":
        dfs(row, col-1)

    if row < 4 and not visited[row+1][col] and graph[row+1][col] == "0":
        dfs(row+1, col)

    if row > 0 and not visited[row-1][col] and graph[row-1][col] == "0":
        dfs(row-1, col)


t = int(raw_input())

for i in range(t):

    graph = []
    visited = []

    count = 0
    while count < 5:

        new_row = str(raw_input()).split()
        if len(new_row) > 0:
            count = count + 1
            graph.append(new_row)
            visited.append([False] * 5)

    dfs(0, 0)

    if visited[4][4]:
        print "COPS"
    else:
        print "ROBBERS"
