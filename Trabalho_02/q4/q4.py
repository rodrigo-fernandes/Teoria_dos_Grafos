#Leonardo Fronza e Rodrigo Fernandes
from heapq import heappush, heappop
from functools import reduce
V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
E = [('A', 'M', 15.91), ('A', 'B', 5.42), ('B', 'C', 2.65), ('B', 'G', 10.48),
     ('C', 'G', 6.75), ('H', 'L', 5.71), ('C', 'D', 5.45), ('D', 'F', 3.33),
     ('F', 'H', 5.52), ('G','H', 0.22), ('D', 'E', 4.69), ('F', 'E', 2.56),
     ('E', 'I', 4.67), ('I', 'J', 3.59), ('J', 'K', 0.78), ('K', 'L', 5.83),
     ('L', 'M', 6.66)]

def make_undirected_graph(E):
    len_E = len(E)
    for i in range(len_E):
        E.append((E[i][1], E[i][0], E[i][2]))

make_undirected_graph(E)

def find_vertexes_odd_degree(E):
    degrees = {}
    for e in E:
        if e[0] in degrees:
            degrees[e[0]] += 1
        else:
            degrees[e[0]] = 1
    vertexes_odd_degree = []
    for v in degrees.keys():
        if degrees[v] % 2 != 0:
            vertexes_odd_degree.append(v)
    return vertexes_odd_degree

def is_euler_graph(E):
    odd_degree_vertexes = find_vertexes_odd_degree(E)
    is_euler = len(odd_degree_vertexes) == 0
    if is_euler:
        print("Grafo é euleriano")
    else:
        print("Grafo não é euleriano pois os vértices {} possuem grau ímpar".format(odd_degree_vertexes))
    return is_euler

def dijkstra(source, target, V, E):
    parent = {}
    distance = {}
    edges = {}
    for v in V:
        parent[v] = None
        distance[v] = 999999
        edges[v] = []
    for e in E:
        edges[e[0]].append((e[1], e[2]))
    distance[source] = 0
    v = source
    Q = []
    heappush(Q, (0, source))
    while len(Q) > 0:
        v = heappop(Q)[1]
        for e in edges[v]:
            if (distance[v] + e[1] < distance[e[0]]):
                parent[e[0]] = v
                distance[e[0]] = distance[v] + e[1]
                heappush(Q, (distance[e[0]], e[0]))
    parents = [target]
    path_distance = distance[target]
    while parent[target] != None:
        parents.append(parent[target])
        target = parent[target]
    return (path_distance, parents)

def eulerize(V, E):
    print("\n==========================\n")
    print("Iniciando processo de adição de arestas para tornar o grafo em euleriano\n")
    odd_degree_vertexes = find_vertexes_odd_degree(E)
    paths = []
    pairs = []
    print("Montando pares de vértices de grau ímpar para execução do dijkstra\n")
    for i in range(len(odd_degree_vertexes)):
        for k in range(i + 1, len(odd_degree_vertexes)):
            pairs.append((odd_degree_vertexes[i], odd_degree_vertexes[k]))
    print("Os pares de vértices definidos para execução do dijkstra são: {}\n".format(pairs))
    paths = []
    for p in pairs:
        print("Executando dijkstra para o par ({},{})".format(p[0],p[1]))
        path = dijkstra(p[0], p[1], V, E)
        print("Caminho encontrado: {}".format(path))
        heappush(paths, path)
    odd_degree_vertexes_dict = {}
    for v in odd_degree_vertexes:
        odd_degree_vertexes_dict[v] = True
    edges = {}
    for v in V:
        edges[v] = {}
    for e in E:
        edges[e[0]][e[1]] = e[2]
    print("\n==========================\n")
    print("Iniciando adição das arestas com base nos caminhos mais curtos encontrados na etapa anterior. Os caminhos foram colocados em ordem ascendente de custo de travessia\n")
    while len(paths) > 0:
        path = heappop(paths)[1]
        v_first = path[0]
        v_last = path[-1]
        if (not v_first in odd_degree_vertexes_dict.keys()) or (not v_last in odd_degree_vertexes_dict.keys()):
            print("-- Caminho {} não será duplicado pois faz a ligação entre os vértices {} e {} sendo que um ou ambos já teve seu grau transformado em par anteriormente\n".format(path, v_first, v_last))
            continue 
        print("++ Caminho {} será duplicado para ligar os vértices {} e {} e assim tornar o grau destes vértices par\n".format(path, v_first, v_last))
        del odd_degree_vertexes_dict[v_first]
        del odd_degree_vertexes_dict[v_last]
        pairs = list(zip(path, path[1:]))
        for pair in pairs:
            E.append((pair[0], pair[1], edges[pair[0]][pair[1]]))
            E.append((pair[1], pair[0], edges[pair[0]][pair[1]]))
    print("Processo de duplicação de arestas finalizado")

def dfs(source, edges, visited):
    for e in edges[source].keys():
        if not visited[e]:
            visited[e] = True
            dfs(e, edges, visited)

def is_bridge(edges, source):
    visited = {}
    for v in edges.keys():
        visited[v] = False
    visited[source] = True
    dfs(source, edges, visited)
    for v in visited:
        if v == False:
            return True
    return False

print("Vértices: {}\n".format(V))
print("Arestas: {}\n".format(E))
if not (is_euler_graph(E)):
    eulerize(V, E)
    print("\n==========================\n")
    print("Iniciando execução do algoritmo de fleury\n")
    edges = {}
    for v in V:
        edges[v] = {}
    for e in E:
        if e[1] in edges[e[0]]:
            edges[e[0]][e[1]].append(e[2])
        else:
            edges[e[0]][e[1]] = [e[2]]
    v = V[0]
    path = [v]
    cost = []
    while len(edges.keys()) > 0:
        keys = list(edges[v].keys()).copy()
        if len(keys) == 0:
            break
        for k in keys:
            if len(edges[v][k]) > 1:
                weight = edges[v][k].pop()
                print("Removendo aresta ({}, {}) de peso {}".format(v,k,weight))
                cost.append(weight)
                edges[k][v].pop()
                path.append(k)
                v = k
                break
            if len(edges[v].keys()) == 1:
                weight = edges[k][v][0]
                print("Removendo aresta ({}, {}) de peso {}".format(v,k,weight))
                cost.append(weight)
                del edges[v]
                del edges[k][v]
                path.append(k)
                v = k
                break
            bkp_vk = edges[v][k].pop()
            bkp_kv = edges[k][v].pop()
            del edges[v][k]
            del edges[k][v]
            if is_bridge(edges, k):
                print("\nAresta ({},{}) não será removida pois separaria o grafo em dois componentes conexos\n".format(v,k))
                edges[v][k] = [bkp_vk]
                edges[k][v] = [bkp_kv]
                continue
            weight = bkp_vk
            print("Removendo aresta ({}, {}) de peso {}".format(v,k,weight))
            cost.append(weight)
            path.append(k)
            v = k
            break
    print("\nCaminho identificado: {}\n".format(path))
    print("Custo calculado: {} = {}\n".format(reduce(lambda x,y: "{} + {}".format(x, y), list(map(lambda x: str(x), cost))), reduce(lambda x,y: x + y, cost)))
