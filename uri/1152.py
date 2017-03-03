# encoding: utf-8


# Nesse problema temos um grafo com pesos.
# O número de vértices que no problema é chamado de 'm' pode chegar até 200000.
# Se você tentar alocar isso numa matriz normal não irá conseguir, são muitos vértices.
# Você consegue facilmente guardar numa variável a soma de todos os custos.
# Pois bem, o problema quer o máximo valor diário que o governo pode economizar.
# Uma das formas de resolver esse problema é utilizar Kruskal, porque vai te retornar o custo total da árvore geradora mínima.
# Tendo esse custo, então é só calcular a diferença entre a soma de todos os custos com o custo retornado pelo algoritmo.


# OBJECT ROAD

class Road:
    def __init__(self, point_1, point_2, meters):
        self.point_1 = point_1
        self.point_2 = point_2
        self.meters = meters


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
    roads.sort(key=lambda x: x.meters)
    union_find = UnionFind(vertices + 1)

    for i in range(edges):
        if not union_find.same_set(roads[i].point_1, roads[i].point_2):
            cost = cost + roads[i].meters
            union_find.connect(roads[i].point_1, roads[i].point_2)

    return cost


## FLOW STARTS HERE

m, n = map(int, raw_input().split())

while m != 0 and n != 0:

    roads = []
    total_cost = 0
    for i in range(n):
        x, y, z = map(int, raw_input().split())
        road = Road(x, y, z)
        roads.append(road)
        total_cost = total_cost + z

    economia = total_cost - kruskal(m, n)
    print economia

    m, n = map(int, raw_input().split())