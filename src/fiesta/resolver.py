# src/fiesta/resolver.py
from .utils import matriz_a_lista_adyacencia, es_arbol_enraizado_adj
from .voraz import resolver_fiesta_voraz
from .dp_arbol import resolver_fiesta_dp_arbol_adj


def resolver_fiesta(matriz, convivencias):
    adj = matriz_a_lista_adyacencia(matriz)
    es_arbol, raiz = es_arbol_enraizado_adj(adj)
    if es_arbol:
        invitados, suma = resolver_fiesta_dp_arbol_adj(adj, convivencias, raiz)
    else:
        invitados, suma = resolver_fiesta_voraz(matriz, convivencias)

    print("\U0001F50D Invitados seleccionados:", [i for i, v in enumerate(invitados) if v])
    print("\U0001F4CA Suma total de convivencia:", suma)
    return invitados, suma