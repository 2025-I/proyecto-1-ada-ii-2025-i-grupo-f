# src/fiesta/resolver_fiesta.py

# src/fiesta/resolver.py

from .dp_arbol import resolver_fiesta_dp_arbol
from .voraz import resolver_fiesta_voraz
from .fuerza_bruta import resolver_fiesta_fuerza_bruta


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
    """
    resultado_dp = resolver_fiesta_dp_arbol(matriz, convivencias)
    resultado_voraz = resolver_fiesta_voraz(matriz, convivencias)
    resultado_fb = resolver_fiesta_fuerza_bruta(matriz, convivencias)

    return {
        'dp': resultado_dp,
        'voraz': resultado_voraz,
        'fuerza_bruta': resultado_fb
    }
