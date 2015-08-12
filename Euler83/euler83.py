from collections import namedtuple
from pprint import pprint as pp
 
 
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
 
class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
 
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = [], dest
        while previous[u]:
            s.insert(0, u)
            u = previous[u]
        s.insert(0, u)
        return s
 
 
 
def compress():
  rows = []
  with open('euler82Data') as f:
    for line in f:
      rows.append([int(i) for i in line.rstrip('\n').split(",")])
  n = len(rows)
  # for i in xrange(n):
  #   rows[i][1] += rows[i][0]
  #   rows[i].remove(rows[i][0]) 
  return rows

table = compress()

def turnToGraph(): 
  table = compress()
  graph = ([])
  n = len(table)
  m = len(table[0])
  for i in xrange(n): 
    for j in xrange(m):
      if j < m-1:
        graph.append((str([i,j]), str([i,j+1]), table[i][j+1]))
      if i < n-1:
        graph.append((str([i,j]), str([i+1,j]), table[i+1][j]))
      if i > 0:
        graph.append((str([i,j]), str([i-1,j]), table[i-1][j]))
      if j > 0:
        graph.append((str([i,j]), str([i,j-1]), table[i][j-1]))
  return graph 

value = turnToGraph()

graph2 = Graph(value)

test = graph2.dijkstra("[0, 0]", "[79, 79]")

testValue = 0
for x in test:
  if len(x) == 6:
    a = x[1]
    b = x[4]
  if len(x) == 7:
    a = x[1]
    b = x[4:6]
  if len(x) == 8: 
    a = x[1:3]
    b = x[5:7]
  testValue += table[int(a)][int(b)]  
print testValue