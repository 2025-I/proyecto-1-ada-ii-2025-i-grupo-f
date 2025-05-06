# src/fiesta/resolver_fiesta.py

# src/fiesta/resolver.py

from .dp_arbol import resolver_fiesta_dp_arbol
from .voraz import resolver_fiesta_voraz
from .fuerza_bruta import resolver_fiesta_fuerza_bruta
#from .utils import matriz_a_lista_adyacencia, es_arbol_enraizado_adj
from time import perf_counter

def resolver_fiesta(matriz, convivencias):
    """
    Ejecuta los tres métodos disponibles:
    - Programación dinámica en árboles (DP)
    - Voraz
    - Fuerza bruta

    Retorna:
        dict con los resultados de cada método:
        {
            'dp': (lista_binaria, suma),
            'voraz': (lista_binaria, suma),
            'fuerza_bruta': (lista_binaria, suma)
        }

    como tenemos una funcion que valida si el grafo es un árbol, podemos usarla para validar
     adj = matriz_a_lista_adyacencia(matriz)
    es_arbol, raiz = es_arbol_enraizado_adj(adj)

    if not es_arbol:
        raise ValueError("❌ Entrada inválida: la matriz no representa un árbol enraizado")    
    """
    # Medición DP
    start_dp = perf_counter()
    resultado_dp = resolver_fiesta_dp_arbol(matriz, convivencias)
    end_dp = perf_counter()
    # Medición Voraz
    start_vz = perf_counter()
    resultado_voraz = resolver_fiesta_voraz(matriz, convivencias)
    end_vz = perf_counter()
    # Medición Fuerza Bruta
    start_fb = perf_counter()
    resultado_fb = resolver_fiesta_fuerza_bruta(matriz, convivencias)
    end_fb = perf_counter()
     # Mostrar tiempos
    print(f"\n⏱ TIEMPOS DE EJECUCIÓN")
    print(f"DP:           {end_dp - start_dp:.6f} s")
    print(f"Voraz:        {end_vz - start_vz:.6f} s")
    print(f"Fuerza bruta: {end_fb - start_fb:.6f} s")
    return {
        'dp': resultado_dp,
        'voraz': resultado_voraz,
        'fuerza_bruta': resultado_fb
    }
