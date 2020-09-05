#Leonardo Fronza e Rodrigo Fernandes
#segue o pai do vértice até chegar no conjunto ao qual ele foi atribuido
def get_super_parent(vertexes, v):
    parent = v
    while (vertexes[parent]["parent"] != None):
        parent = vertexes[parent]["parent"]
    return parent

def link(vertexes, v1, v2):
    v1_parent = get_super_parent(vertexes, v1)
    v2_parent = get_super_parent(vertexes, v2)
    #caso os vértices estejam no mesmo conjunto não há o que fazer
    if v1_parent == v2_parent:
        return
    if len(vertexes[v1_parent]["letters"]) < len(vertexes[v2_parent]["letters"]):
        from_v = v1_parent
        to_v = v2_parent
    else:
        from_v = v2_parent
        to_v = v1_parent
    #move os vértices do conjunto com menos vértices
    #para o conjunto com mais vértices
    while len(vertexes[from_v]["letters"]) > 0:
        vertexes[to_v]["letters"].append(vertexes[from_v]["letters"].pop())
    vertexes[from_v]["parent"] = to_v

N = int(input()) #número de casos
for n in range(N):
    #V = número de vértices
    #E = número de arestas
    V, E = list(map(int, input().split()))
    vertexes = {}
    for i in range(V):
        #cria um conjunto para cada vértice
        vertexes[chr(ord('a') + i)] = {"letters": [chr(ord('a') + i)], "parent": None}
    for _ in range(E):
        v1, v2 = input().split()
        #conecta os vértices colocando um como pai do outro e movendo
        #a(s) letra(s) do filho para o pai
        link(vertexes, v1, v2)
    print("Case #{0}:".format(n + 1))
    n_connected_components = 0
    for v in list(vertexes.keys()):
        if len(vertexes[v]["letters"]) != 0:
            #incrementa o número de componentes caso o conjunto da letra não esteja vazio
            n_connected_components += 1
            #imprime os vértices que formam um componente conexo
            vertexes[v]["letters"].sort()
            print(','.join(map(str, vertexes[v]["letters"])) + ',')
    print("{0} connected components\n".format(n_connected_components))
print()
