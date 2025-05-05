# src/fiesta.py

"""
Objetivos:
1. Ningún invitado supervisa a otro invitado.
2. Ningún invitado es supervisado por otro invitado.
3. Nadie que se supervise a sí mismo puede ir.
4. Se maximiza la suma total de convivencia.
5.Puesto por nosotros, dectetar si es un arbol.
"""

# --- Método Voraz para grafos generales (ciclos permitidos) ---
def resolver_fiesta_voraz(matriz, convivencias):
    n = len(matriz) #cantidad de empleados 
    empleados = list(range(n)) #Crea una lista con los índices de todos los empleados: [0, 1, 2, ..., n-1].
    # Paso 1: Crear listas para registrar supervisiones
    supervisa = [set() for _ in range(n)]   #  empleados que son supervisados por i
    supervisado_por = [set() for _ in range(n)] # quién supervisa a j
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j]==1:
                supervisa[i].add(j) #Se agrega j al conjunto supervisa[i].
                supervisado_por[j].add(i) #Se agrega i al conjunto supervisado_por[j].

    # Paso 2: Ordenar empleados por mayor convivencia (descendente)
    #
    empleados.sort(key=lambda x: convivencias[x], reverse=True)
    # Paso 3: Seleccionar invitados evitando conflictos
    invitados = [0] * n #5 → [0, 0, 0, 0, 0]
    incompatibles = set() # los que no pueden ser invitados

    for i in empleados: 
        if i in incompatibles:
            continue
        if matriz[i][i] == 1:  # se supervisa a sí mismo
            continue
        invitados[i] = 1

        # Marcar como incompatibles a quienes él supervisa o lo supervisan
        incompatibles.update(supervisa[i])
        incompatibles.update(supervisado_por[i])
        incompatibles.add(i)
     # Paso 4: Calcular la suma de convivencia de los invitados
    suma = sum(convivencias[i] for i in range(n) if invitados[i])

    return invitados, suma

# --- Método DP para árboles (sin ciclos, raíz única) ---
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

        return (
            incluir_suma,
            excluir_suma,
            incluir_invitados,
            excluir_invitados
        )

    inc, exc, invit_inc, invit_exc = dp(raiz)
    final_invitados = invit_inc if inc > exc else invit_exc
    invitados = [0] * n
    for i in final_invitados:
        invitados[i] = 1
    suma = sum(convivencias[i] for i in final_invitados)
    return invitados, suma

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