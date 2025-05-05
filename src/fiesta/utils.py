# src/fiesta/utils.py

def matriz_a_lista_adyacencia(matriz):
    """
    Convierte una matriz de adyacencia en una lista de adyacencia.
    """
    n = len(matriz)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                adj[i].append(j)
    return adj


def es_arbol_enraizado_adj(adj_list):
    n = len(adj_list)
    in_degree = [0] * n

    print("\n🔍 Validando árbol enraizado...")
    print("Adj list recibida:", adj_list)

    for i in range(n):
        for j in adj_list[i]:
            in_degree[j] += 1

    print("In-degree:", in_degree)

    raices = [i for i, grado in enumerate(in_degree) if grado == 0]
    print("Raíces encontradas:", raices)

    if len(raices) != 1:
        print("❌ Árbol inválido: múltiples o ninguna raíz")
        return False, None

    raiz = raices[0]

    visitado = [False] * n

    def dfs(v):
        visitado[v] = True
        for u in adj_list[v]:
            if not visitado[u]:
                dfs(u)

    dfs(raiz)

    print("Nodos visitados desde la raíz:", visitado)

    if not all(visitado):
        print("❌ Árbol inválido: no todos los nodos fueron visitados")
        return False, None

    print("✅ Árbol válido. Raíz:", raiz)
    return True, raiz

