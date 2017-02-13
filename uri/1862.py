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


def first_execution():
    for i in range(n):
        if visited[i].count(True) == 0:
            return (i, i)


def check():
    qnt = len(modified)
    for i in range(n):
        if i in modified:
            if visited[i].count(True) != qnt:
                return False
        else:
            if visited[i].count(True) == 0:
                return (i, i)
    return NONE




# FLOW STARTS HERE


n = int(raw_input())
graph = []
visited = []
queue = qq.Queue()
NONE = "NONE"

for vez in range(n):
    new_row = list(str(raw_input()))
    graph.append(new_row)
    visited.append([False] * n)


tam_families = []
other_family = first_execution()
checked = True
while other_family != NONE:

    modified = []

    row = other_family[0]
    col = other_family[1]

    modified.append(row)

    dfs(row, col)

    n_people = str( len(modified) )
    tam_families.append(n_people)

    other_family = check()

    if other_family == False:
	checked = False
        break


if checked:
    print len(tam_families)
    print " ".join(tam_families)
else:
    print "-1"