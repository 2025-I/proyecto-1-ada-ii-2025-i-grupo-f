from typing import List, Tuple, Dict

def resolver_fiesta(m: int, matriz: List[List[int]], calificaciones: List[int]) -> Tuple[List[int], int]:
    # Paso 1: Construir grafo de supervisión
    hijos: Dict[int, List[int]] = {i: [] for i in range(m)}
    tiene_padre = [False] * m

    for i in range(m):
        for j in range(m):
            if matriz[i][j] == 1:
                hijos[i].append(j)
                tiene_padre[j] = True

    # Paso 2: Encontrar raíces
    raices = [i for i in range(m) if not tiene_padre[i]]
    if not raices:
        raices = list(range(m))  # por si todo es un ciclo

    memo = {}

    # Paso 3: DP con prevención de ciclos
    def dp(nodo: int, visitados: set) -> Tuple[int, int]:
        if nodo in visitados:
            return (0, 0)

        if nodo in memo:
            return memo[nodo]

        visitados.add(nodo)
        incluir = calificaciones[nodo]
        excluir = 0
        for h in hijos[nodo]:
            inc_h, exc_h = dp(h, visitados.copy())
            incluir += exc_h
            excluir += max(inc_h, exc_h)
        memo[nodo] = (incluir, excluir)
        return memo[nodo]

    invitados = [0] * m

    # Paso 4: reconstrucción de solución con prevención de ciclos
    def reconstruir(nodo: int, incluir_padre: bool, visitados: set):
        if nodo in visitados:
            return
        visitados.add(nodo)

        incluir, excluir = memo[nodo]
        if incluir_padre:
            invitados[nodo] = 0
            for h in hijos[nodo]:
                reconstruir(h, False, visitados)
        else:
            if incluir > excluir:
                invitados[nodo] = 1
                for h in hijos[nodo]:
                    reconstruir(h, True, visitados)
            else:
                invitados[nodo] = 0
                for h in hijos[nodo]:
                    reconstruir(h, False, visitados)

    # Aplicar DP y reconstrucción para cada raíz
    for r in raices:
        dp(r, set())
        reconstruir(r, False, set())

    total = sum(calificaciones[i] for i in range(m) if invitados[i] == 1)
    return invitados, total
