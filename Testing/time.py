import time


# f(a, b, c) on line 11 corresponds to whatever parameters function f runs under, also reflected in the a, b, c of line 6.
# f: function
# n: iterations
# a,b,c,etc: parameters of 

def timing(f, n, a, b, c):
    print f.__name__,
    r = range(n)
    t1 = time.clock()
    for i in r:
        f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c); f(a, b, c)
    t2 = time.clock()
    print round(t2-t1, 3)
    



graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
        

print timing(find_path, 100000, graph, 'A', 'B')

 