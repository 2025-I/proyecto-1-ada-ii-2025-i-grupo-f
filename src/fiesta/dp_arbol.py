# src/fiesta/dp_arbol.py

from .utils import matriz_a_lista_adyacencia, es_arbol_enraizado_adj

def resolver_fiesta_dp_arbol(matriz, convivencias):
    adj = matriz_a_lista_adyacencia(matriz)
    es_arbol, raiz = es_arbol_enraizado_adj(adj)
    if not es_arbol:
        return [0] * len(matriz), 0

    n = len(matriz)

    def dp(v):
        incluir = convivencias[v]
        excluir = 0
        invitados_incluir = [0] * n
        invitados_excluir = [0] * n
        invitados_incluir[v] = 1

        for hijo in adj[v]:
            inc, exc, inv_inc, inv_exc = dp(hijo)

            incluir += exc  # si invito a v, no puedo invitar a hijos
            for i in range(n):
                invitados_incluir[i] += inv_exc[i]

            if inc > exc:
                excluir += inc
                for i in range(n):
                    invitados_excluir[i] += inv_inc[i]
            else:
                excluir += exc
                for i in range(n):
                    invitados_excluir[i] += inv_exc[i]

        return incluir, excluir, invitados_incluir, invitados_excluir

    incluir, excluir, invitados_incluir, invitados_excluir = dp(raiz)
    if incluir > excluir:
        return invitados_incluir, incluir
    else:
        return invitados_excluir, excluir
