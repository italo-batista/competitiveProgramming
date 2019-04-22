import sys
sys.path.append('./datastructures')
from datastructures import GraphNode
sys.path.append('./algorithms')
from algorithms import bfs

def route_between_nodes(source, target):
    bfs(source)
    return target.visited


if __name__ == '__main__':  # tests

    nodeA = GraphNode('A')
    nodeB = GraphNode('B')
    nodeC = GraphNode('C')
    nodeD = GraphNode('D')
    nodeE = GraphNode('E')
    nodeF = GraphNode('F')

    nodeA.add_adj(nodeB)
    nodeA.add_adj(nodeC)
    nodeC.add_adj(nodeD)
    nodeD.add_adj(nodeE)
    nodeD.add_adj(nodeF)

    assert route_between_nodes(nodeA, nodeE) is True

