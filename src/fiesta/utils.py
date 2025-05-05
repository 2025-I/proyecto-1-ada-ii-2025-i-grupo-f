# src/fiesta/utils.py
def matriz_a_lista_adyacencia(matriz):
    n = len(matriz)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                adj[i].append(j)
    return adj

def es_arbol_enraizado_adj(adj_list):
    n = len(adj_list)
    padres = [0] * n
    for u in range(n):
        for v in adj_list[u]:
            padres[v] += 1
    raices = [i for i, p in enumerate(padres) if p == 0]
    if len(raices) != 1:
        return False, None

    visitado = [False] * n
    ciclo = [False]

    def dfs(v):
        if visitado[v]:
            ciclo[0] = True
            return
        visitado[v] = True
        for u in adj_list[v]:
            dfs(u)

    dfs(raices[0])
    if all(visitado) and not ciclo[0]:
        return True, raices[0]
    return False, None