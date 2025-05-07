# src/fiesta/fuerza_bruta.py
from itertools import combinations


def es_valido(subconjunto, matriz):
    for i in subconjunto:
        for j in subconjunto:
            if i != j and matriz[i][j] == 1:
                return False  # i supervisa a j
    return True

def resolver_fiesta_fuerza_bruta(matriz, convivencias):
    n = len(matriz)
    mejor_suma = 0
    mejor_inv = [0] * n

    # Revisar todos los subconjuntos posibles
    for e in range(1, n + 1):
        for subconjunto in combinations(range(n), e):
            if es_valido(subconjunto, matriz):
                suma = sum(convivencias[i] for i in subconjunto)
                if suma > mejor_suma:
                    mejor_suma = suma
                    subconjunto_set = set(subconjunto)
                    mejor_inv = [1 if i in subconjunto_set else 0 for i in range(n)]

    return mejor_inv , mejor_suma