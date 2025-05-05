# src/fiesta/dp_arbol.py
def resolver_fiesta_dp_arbol_adj(adj_list, convivencias, raiz):
    n = len(adj_list)
    invalido = [False] * n
    for i in range(n):
        if i in adj_list[i]:
            invalido[i] = True

    def dp(v):
        if invalido[v]:
            return (0, 0, [], [])

        incluir_suma = convivencias[v]
        excluir_suma = 0
        incluir_invitados = [v]
        excluir_invitados = []

        for h in adj_list[v]:
            inc_h, exc_h, invit_inc, invit_exc = dp(h)
            incluir_suma += exc_h
            incluir_invitados += invit_exc
            if inc_h > exc_h:
                excluir_suma += inc_h
                excluir_invitados += invit_inc
            else:
                excluir_suma += exc_h
                excluir_invitados += invit_exc

        return incluir_suma, excluir_suma, incluir_invitados, excluir_invitados

    inc, exc, invit_inc, invit_exc = dp(raiz)
    final_invitados = invit_inc if inc > exc else invit_exc
    invitados = [0] * n
    for i in final_invitados:
        invitados[i] = 1
    suma = sum(convivencias[i] for i in final_invitados)
    return invitados, suma
