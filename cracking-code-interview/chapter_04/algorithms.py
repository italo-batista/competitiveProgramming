import sys
sys.path.append('./datastructures')
from datastructures import GraphNode


def dfs(root):
    # type (GraphNode)

    if root or root.visited:
        return

    root.visited = True

    for child in root.children:
        dfs(child)


def bfs(root):
    # type (GraphNode)

    queue = []
    queue.append(root)

    while len(queue) > 0:
        top = queue.pop(False)
        if not top.visited:
            top.visited = True
            for adj in top.adjacents:
                queue.append(adj)
