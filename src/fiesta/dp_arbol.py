# src/fiesta/dp_arbol.py

from .utils import matriz_a_lista_adyacencia, es_arbol_enraizado_adj
import sys
sys.setrecursionlimit(100_000)  # Aumentamos el límite para árboles grandes
def resolver_fiesta_dp_arbol(matriz, convivencias):
    adj = matriz_a_lista_adyacencia(matriz)
    es_arbol, raiz = es_arbol_enraizado_adj(adj)
    if not es_arbol:
        return [0] * len(matriz), 0

    def dp(v):
        incluir_suma = convivencias[v]
        excluir_suma = 0

        incluir_set = {v}
        excluir_set = set()

        for hijo in adj[v]:
            inc_s, exc_s, inc_set, exc_set = dp(hijo)

            # Si invito a v, no puedo invitar a hijos
            incluir_suma += exc_s
            incluir_set |= exc_set  # unión con los que se pueden incluir al excluir hijos

            # Caso excluir v: elijo mejor opción de cada hijo
            if inc_s > exc_s:
                excluir_suma += inc_s
                excluir_set |= inc_set
            else:
                excluir_suma += exc_s
                excluir_set |= exc_set

        return incluir_suma, excluir_suma, incluir_set, excluir_set

    inc, exc, inc_set, exc_set = dp(raiz)

    if inc > exc:
        invitados_set = inc_set
        total = inc
    else:
        invitados_set = exc_set
        total = exc

    n = len(matriz)
    binario = [1 if i in invitados_set else 0 for i in range(n)]
    return binario, total