import sys
sys.setrecursionlimit(10000)

n, m = map(int, raw_input().split())

matriz = []
for i in xrange(n):
    matriz.append(raw_input())

# ninguem foi visitado ainda
vis = [[0 for i in xrange(m)] for j in xrange(n)]


def check(i, j, i2, j2):
    if i >= n or j >= m or i < 0 or j < 0:
        return False
    if matriz[i][j] != matriz[i2][j2]:
        return False
    return i != i2 or j != j2


direcoes = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(i, j, par_i, par_j):
    if vis[i][j]:
        return True

    vis[i][j] = 1

    for inc_i, inc_j in direcoes:
        new_i = i + inc_i
        new_j = j + inc_j
        if check(new_i, new_j, par_i, par_j) and dfs(new_i, new_j, i, j):
            return True

    return False


flag = False
for i in xrange(n):
    for j in xrange(m):
        if not vis[i][j]:
            if dfs(i, j, i, j):
                print 'Yes'
                flag = True
                break
    if flag:
        break

if not flag:
    print 'No'