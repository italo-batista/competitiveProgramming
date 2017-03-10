# OBJECT EDGE

class Edge:
    def __init__(self, point_1, point_2, weight):
        self.point_1 = point_1
        self.point_2 = point_2
        self.weight = weight


# STRUCTURE UNION_FIND

class UnionFind:
    def __init__(self, tam):
        self.parents = range(tam + 1)
        self.sizes = [1] * (tam + 1)

    def get_parent(self, x):
        if x == self.parents[x]:
            return self.parents[x]
        else:
            self.parents[x] = self.get_parent(self.parents[x])
            return self.parents[x]

    def same_set(self, x, y):
        return self.get_parent(x) == self.get_parent(y)

    def connect(self, x, y):

        if not self.same_set(x, y):

            if self.sizes[self.get_parent(x)] > self.sizes[self.get_parent(y)]:
                self.parents[self.get_parent(y)] = self.get_parent(x)
                self.sizes[self.get_parent(x)] += self.sizes[self.get_parent(y)]

            else:
                self.parents[self.get_parent(x)] = self.get_parent(y)
                self.sizes[self.get_parent(y)] += self.sizes[self.get_parent(x)]

    def get_size(self, x):
        return self.sizes[self.get_parent(x)]


# ALGORITHM

def kruskal(vertices, edges):
    cost = 0
    edges.sort(key=lambda x: x.weight)
    union_find = UnionFind(vertices + 1)

    for i in range(edges):
        if not union_find.same_set(edges[i].point_1, edges[i].point_2):
            cost = cost + edges[i].weight
            union_find.connect(edges[i].point_1, edges[i].point_2)

    return cost


## FLOW STARTS HERE

n_vertices, n_edges = map(int, raw_input().split())

edges = []
for i in range(n_edges):
    point1, point2, weight = map(int, raw_input().split())
    edge = Edge(point1, point2, weight)
    edges.append(edge)

print kruskal(n_vertices, n_edges)
