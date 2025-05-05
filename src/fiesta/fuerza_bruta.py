# src/fiesta/fuerza_bruta.py
from itertools import combinations

def es_valido(subconjunto, matriz):
    for i in subconjunto:
        if matriz[i][i] == 1:
            return False
        for j in subconjunto:
            if i != j and matriz[i][j] == 1:
                return False
    return True

def resolver_fiesta_fuerza_bruta(matriz, convivencias):
    n = len(matriz)
    mejor_suma = 0
    mejor_subconjunto = []

    for r in range(1, n + 1):
        for subconjunto in combinations(range(n), r):
            if es_valido(subconjunto, matriz):
                suma = sum(convivencias[i] for i in subconjunto)
                if suma > mejor_suma:
                    mejor_suma = suma
                    mejor_subconjunto = list(subconjunto)

    invitados = [0] * n
    for i in mejor_subconjunto:
        invitados[i] = 1

    return invitados, mejor_suma