import Queue

n, m = map(int, raw_input().split())

# MONTA GRAFO

grafo = []

for i in range(n+1):
    grafo.append( [ [] for j in range(n+1) ] )


for i in range(m+1):
        x, y, p = map(int, raw_input().split())
        grafo[x][y] = (y, p)



