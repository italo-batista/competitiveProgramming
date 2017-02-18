import Queue as qq
import sys

sys.setrecursionlimit(2090000000) # limite da recursao

def dfs(row, col):

    visited[row][row] = True
    visited[row][col] = True
    visited[col][row] = True

    if row not in modified:
        modified.append(row)

    for i in range(n):
        if not visited[row][i] and graph[row][i] == "S" and row != i:
            dfs(i, row)


def check():
    qnt = len(modified)
    for t in range(n):
        if t in modified:
            if visited[t].count(True) != qnt:
                return False
    return True


# FLOW STARTS HERE


n = int(raw_input())
graph = []
visited = []
queue = qq.Queue()

for vez in range(n):
    new_row = list(str(raw_input()))
    graph.append(new_row)
    visited.append([False] * n)


tam_families = []
checked = True

for l in range(len(graph)):
    for j in range(len(graph[0])):

        if not visited[l][j] and graph[l][j] == "S":

            modified = [l]
            dfs(l, j)

            n_people = str( len(modified) )
            tam_families.append(n_people)

            if not check():
                checked = False
                break

if checked:
    print len(tam_families)
    print " ".join(tam_families)
else:
    print "-1"

