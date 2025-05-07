# src/fiesta/dp_arbol.py

from .utils import matriz_a_lista_adyacencia, es_arbol_enraizado_adj

def resolver_fiesta_dp_arbol(matriz, convivencias):
    adj = matriz_a_lista_adyacencia(matriz)
    es_arbol, raiz = es_arbol_enraizado_adj(adj)
    if not es_arbol:
        return [0] * len(matriz), 0

    n = len(matriz)
    dp_incluir = [0] * n
    dp_excluir = [0] * n

    def dfs(v):
        dp_incluir[v] = convivencias[v]
        for h in adj[v]:
            dfs(h)
            dp_incluir[v] += dp_excluir[h]
            dp_excluir[v] += max(dp_incluir[h], dp_excluir[h])

    dfs(raiz)

    invitados = [0] * n

    def reconstruir(v, incluir):
        if incluir:
            invitados[v] = 1
            for h in adj[v]:
                reconstruir(h, False)
        else:
            for h in adj[v]:
                if dp_incluir[h] > dp_excluir[h]:
                    reconstruir(h, True)
                else:
                    reconstruir(h, False)

    if dp_incluir[raiz] > dp_excluir[raiz]:
        reconstruir(raiz, True)
        return invitados, dp_incluir[raiz]
    else:
        reconstruir(raiz, False)
        return invitados, dp_excluir[raiz]
