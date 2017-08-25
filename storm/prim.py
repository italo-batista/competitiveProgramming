import Queue
import sys

class MyPair():
 
    def __init__(self, key, vertex):
        self.key = key
        self.vertex = vertex
        
	def __getitem__(self):
		return self.key

class Adj():
 
    def __init__(self, vertex, edge):
        self.edge = edge
        self.vertex = vertex        

class PrimAlgorithm():
	
	def __init__(self, graph, vertices):
		
		self.graph = graph   # adjacent list		
		self.vertices = vertices
		self.heap = Queue.PriorityQueue()
		
	def printMST(self):
		
		print "\nEdge \t Weight "
		for v in range(1, self.tam):
			print "%d - %d \t : %d" % (self.parent[v], v, self.key[v])
			
	def init(self):
		
		INF = sys.maxint
		
		self.tam = len(vertices)
		self.mstSet = [False] * self.tam
		self.key = [INF] * self.tam
		self.parent = [None] * self.tam   # Array to store constructed MST
		
		first_vertex = self.vertices[0]		
		pair = MyPair(0, first_vertex)		
		
		self.heap.put(pair)
		self.mstSet[0] = True
		self.key[0] = 0
		self.parent[0] = -1
		
	def minKey(self, key, mstSet):
		
		# Initilaize min value
		minn = sys.maxint

		for v in range(self.tam):
			if key[v] < minn and mstSet[v] == False:
				minn = key[v]
				min_index = v

		return min_index		
				
	def findMST(self):
		
		self.init()
		
		#while (not self.heap.empty()):
			#minimum = self.heap.get()
			#u = minimum.vertex
		
		for cout in range(self.tam):			
			u = self.minKey(self.key, self.mstSet)						
			self.mstSet[u] = True
			
			for adj in graph[u]:
				
				v = adj.vertex
				w = adj.edge
				
				if self.mstSet[v] == False and self.key[v] > w:
					
					self.key[v] = w
					self.parent[v] = u
					
					pair = MyPair(w, v)
					self.heap.put(pair)
					#self.mstSet[v] = True
					
		self.printMST()


### FLOW INITS HERE

N, M = map(int, raw_input().split())

vertices = range(N)
graph = [[] for i in range(N)]

for i in xrange(M):
	
	v1, v2, w = map(int, raw_input().split())
	
	adj = Adj(v2, w)
	graph[v1].append(adj)
	
	adj = Adj(v1, w)
	graph[v2].append(adj)

mst = PrimAlgorithm(graph, vertices)
mst.findMST()




#6 9
#0 1 2
#1 2 3
#2 3 9
#3 4 4
#4 5 4
#5 0 5
#0 4 1
#1 4 7
#2 4 3

#Edge 	 Weight 
#0 - 1 	 : 2
#4 - 2 	 : 3
#4 - 3 	 : 4
#0 - 4 	 : 1
#4 - 5 	 : 4

#-

#9 14
#0 1 4
#0 7 8
#1 2 8
#1 7 11
#2 3 7
#2 5 4
#2 8 2
#3 4 9
#3 5 14
#5 4 10
#6 5 2
#7 6 1
#7 8 7
#8 6 6

#Edge 	 Weight 
#0 - 1 	 : 4
#1 - 2 	 : 8
#2 - 3 	 : 7
#3 - 4 	 : 9
#2 - 5 	 : 4
#5 - 6 	 : 2
#6 - 7 	 : 1
#2 - 8 	 : 2

#-

#0 1 2
#0 3 6
#1 2 3
#1 3 8
#1 4 5
#2 4 7
#2 4 9

#Edge 	 Weight 
#0 - 1 	 : 2
#1 - 2 	 : 3
#0 - 3 	 : 6
#1 - 4 	 : 5
