t = int(raw_input())

for i in range(t):

    def row_col(num):
        row = num / tam
        col = num % tam
        return(row, col)

    n = int(raw_input())
    v, a = map(int, raw_input().split())

    grafo = []

    for i in range(v):
        grafo.append([])

    for i in range(a):
        pi, pii = map(int, raw_input().split())
        if pii not in grafo[pi]:
            grafo[pi].append(pii)
        if pi not in grafo[pii]:
            grafo[pii].append(pi)

    c = 0
    for i in range(v):
        c += len(grafo[i])

    print c