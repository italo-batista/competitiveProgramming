import Queue

while True:

    n, m = map(int, raw_input().split())

    if n == 0 and m == 0: break


    def print_ajd(row, col):

        if col > 0:
            if not visited[row][col - 1] and graph[row][col-1] == "A":
                graph[row][col - 1] = "T"
                contamined.put((row, col - 1))

        if col < (m - 1):
            if not visited[row][col + 1] and graph[row][col + 1] == "A":
                graph[row][col + 1] = "T"
                contamined.put((row, col + 1))

        if row > 0:
            if not visited[row - 1][col] and graph[row - 1][col] == "A":
                graph[row - 1][col] = "T"
                contamined.put((row - 1, col))

        if row < (n - 1):
            if not visited[row + 1][col] and graph[row + 1][col] == "A":
                graph[row + 1][col] = "T"
                contamined.put((row + 1, col))


    graph = []
    visited = []
    contamined = Queue.Queue()

    for vez in range(n):
        new_row = str(raw_input())
        graph.append( list(new_row) )
        visited.append( [False] * m )

    for i in range(n):
        for j in range(m):
            if graph[i][j] == "T":
                contamined.put((i, j))

    while not contamined.empty():

        no = contamined.get()
        row = no[0]
        col = no[1]

        print_ajd(row, col)
        visited[row][col] = True


    for l in graph:
        print "".join(l)
    print ""