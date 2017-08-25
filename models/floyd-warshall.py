## QUOTE
# Floyd-Warshall gives us the shortest paths from all source to all target
# nodes. There are other uses for Floyd-Warshall as well; it can be used to
# find connectivity in a graph (known as the Transitive Closure of a graph).

INF = float('inf')

def printMatrix(MATRIX):
    for i in range(V):
        for j in range(V):
            if(MATRIX[i][j] == INF):
                print "%7s" %("INF"),
            else:
                print "%7d\t" %(MATRIX[i][j]),
            if j == V-1:
                print ""


## CONSTRUCTING GRAPH

V = input()
my_graph = [[INF for i in range(V)] for i in range(V)]

for i in range(V):
        v1, v2, w = map(int, raw_input().split())
        my_graph[v1][v2] = w


## FLOYD-WARSHALL ALGORITHM

def floydWarshall(graph):

    dp = map(lambda i : map(lambda j : j, i) , graph) # copy graph

    # Base Case
    for i in range(V):
        for j in range(V):
            if i == j:
                dp[i][j] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min( dp[i][j], dp[i][k] + dp[k][j] )
	printMatrix(dp)
	print ""

    distances = dp
    return distances


## PRINTING DISTANCES FOR EVERY PAIR OF VERTICES

dists = floydWarshall(my_graph)
printMatrix(dists)
