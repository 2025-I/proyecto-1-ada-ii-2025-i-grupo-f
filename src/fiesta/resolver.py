# src/fiesta/resolver.py


from .dp_arbol import resolver_fiesta_dp_arbol
from .voraz import resolver_fiesta_voraz
from .fuerza_bruta import resolver_fiesta_fuerza_bruta
from time import perf_counter

def resolver_fiesta(matriz, convivencias):
    """
    Ejecuta los tres métodos disponibles:
    - Programación dinámica en árboles (DP)
    - Voraz
    - Fuerza bruta (solo si el tamaño es ≤ 20)

    Retorna:
        dict con los resultados de cada método:
        {
            'dp': ((lista_binaria, suma), tiempo),
            'voraz': ((lista_binaria, suma), tiempo),
            'fuerza_bruta': ((lista_binaria, suma), tiempo) o None si no se ejecuta
        }
    """

    # DP
    start_dp = perf_counter()
    resultado_dp = resolver_fiesta_dp_arbol(matriz, convivencias)
    end_dp = perf_counter()
    tiempo_dp = end_dp - start_dp

    # Voraz
    start_vz = perf_counter()
    resultado_voraz = resolver_fiesta_voraz(matriz, convivencias)
    end_vz = perf_counter()
    tiempo_vz = end_vz - start_vz

    # Fuerza Bruta (solo si n <= 20)
    n = len(matriz)
    if n <= 20:
        start_fb = perf_counter()
        resultado_fb = resolver_fiesta_fuerza_bruta(matriz, convivencias)
        end_fb = perf_counter()
        tiempo_fb = end_fb - start_fb
    else:
        resultado_fb = None
        tiempo_fb = None

    # Mostrar tiempos
    print("\n⏱ TIEMPOS DE EJECUCIÓN")
    print(f"DP:           {tiempo_dp:.6f} s")
    print(f"Voraz:        {tiempo_vz:.6f} s")
    if tiempo_fb is not None:
        print(f"Fuerza bruta: {tiempo_fb:.6f} s")
    else:
        print("Fuerza bruta: NO EJECUTADO (n > 20)")

    return {
        'dp': (resultado_dp, tiempo_dp),
        'voraz': (resultado_voraz, tiempo_vz),
        'fuerza_bruta': (resultado_fb, tiempo_fb)
    }
