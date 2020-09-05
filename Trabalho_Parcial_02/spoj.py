#Leonardo Fronza, Rodrigo Fernandes

dir = "c:/temp/entrada.in"
f = open(dir, "r")

n, m = map(int, input().split())

total = 0
edges = []
sets = [i for i in range(0, n + 1)]
rank = [0] * (n + 1)

for i in range(0, m):
    u, v, c = map(int, input().split())
    edges.append((c, u , v))

edges = sorted(edges, key = lambda e: e[0])

def parent(sets, e):
    if sets[e] == e:
        return e
    return parent(sets, sets[e])

def union(sets, rank, v, u, parent_v, parent_u):
    if rank[parent_v] < rank[parent_u]: 
        sets[parent_v] = parent_u 
    elif rank[parent_v] > rank[parent_u]: 
        sets[parent_u] = parent_v 
    else : 
        sets[parent_u] = parent_v 
        rank[parent_v] += 1

qt_added_edges = 0

for c, u, v in edges:
    if qt_added_edges >= n - 1:
        break
    parent_v = parent(sets, v)
    parent_u = parent(sets, u)
    if parent_v != parent_u:
        union(sets, rank, v, u, parent_v, parent_u)
        qt_added_edges += 1
        total += c

print(total)
