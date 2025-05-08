import matplotlib.pyplot as plt
import random
import time

from src.fiesta.dp_arbol import resolver_fiesta_dp_arbol
from src.fiesta.voraz import resolver_fiesta_voraz
from src.fiesta.fuerza_bruta import resolver_fiesta_fuerza_bruta  # Agregado

def generar_arbol_enraizado(n):
    matriz = [[0] * n for _ in range(n)]
    for hijo in range(1, n):
        padre = random.randint(0, hijo - 1)
        matriz[padre][hijo] = 1
    return matriz

def generar_convivencias(n, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]

def medir_y_graficar_tiempos(tamanos, repeticiones=5):
    tiempos_dp = []
    tiempos_voraz = []
    tiempos_fuerza_bruta = []

    for n in tamanos:
        print(f"\n⏱ Tamaño {n}: ", end="")
        tiempos_n_dp = []
        tiempos_n_voraz = []
        tiempos_n_fb = []

        for _ in range(repeticiones):
            matriz = generar_arbol_enraizado(n)
            convivencias = generar_convivencias(n)

            if n <= 20:  # Fuerza bruta solo para entradas pequeñas
                t0 = time.perf_counter()
                resolver_fiesta_fuerza_bruta(matriz, convivencias)
                t1 = time.perf_counter()
                tiempos_n_fb.append(t1 - t0)

            t0 = time.perf_counter()
            resolver_fiesta_dp_arbol(matriz, convivencias)
            t1 = time.perf_counter()
            tiempos_n_dp.append(t1 - t0)

            t0 = time.perf_counter()
            resolver_fiesta_voraz(matriz, convivencias)
            t1 = time.perf_counter()
            tiempos_n_voraz.append(t1 - t0)

        promedio_dp = sum(tiempos_n_dp) / repeticiones
        promedio_voraz = sum(tiempos_n_voraz) / repeticiones
        promedio_fb = (sum(tiempos_n_fb) / repeticiones) if tiempos_n_fb else None

        print(f"Voraz {promedio_voraz:.4f}s, DP {promedio_dp:.4f}s", end="")
        if promedio_fb is not None:
            print(f", Fuerza Bruta {promedio_fb:.4f}s")
        else:
            print()

        tiempos_dp.append(promedio_dp)
        tiempos_voraz.append(promedio_voraz)
        tiempos_fuerza_bruta.append(promedio_fb)

    # Curvas teóricas
    valores_teoricos_dp = [n * 1e-6 for n in tamanos]              # O(n)
    valores_teoricos_voraz = [n**2 * 1e-8 for n in tamanos]        # O(n²)
    valores_teoricos_fb = [n**3 * 5e-10 if n <= 20 else None for n in tamanos]  # O(2^n) ≈ O(n^3) para casos chicos

    # Graficar
    plt.plot(tamanos, tiempos_dp, label="DP Árbol (experimental)", marker='o')
    plt.plot(tamanos, tiempos_voraz, label="Voraz (experimental)", marker='x')
    if any(tiempos_fuerza_bruta):
        x_fb = [n for n, t in zip(tamanos, tiempos_fuerza_bruta) if t is not None]
        y_fb = [t for t in tiempos_fuerza_bruta if t is not None]
        plt.plot(x_fb, y_fb, label="Fuerza Bruta (experimental)", marker='s')

    plt.plot(tamanos, valores_teoricos_dp, '--', label="DP O(n) teórico")
    plt.plot(tamanos, valores_teoricos_voraz, '--', label="Voraz O(n²) teórico")
    if any(valores_teoricos_fb):
        x_fb = [n for n, t in zip(tamanos, valores_teoricos_fb) if t is not None]
        y_fb = [t for t in valores_teoricos_fb if t is not None]
        plt.plot(x_fb, y_fb, '--', label="Fuerza Bruta O(n³) teórico")

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos vs complejidad teórica")
    plt.legend()
    plt.grid(True)

    import os
    os.makedirs("docs/imagenes", exist_ok=True)
    plt.savefig("docs/imagenes/tiempos_vs_complejidad.png")
    plt.show()

if __name__ == "__main__":
    tamanos_prueba = [5, 10, 15, 20, 100, 500, 1000, 2000, 5000, 10000, 20000]
    medir_y_graficar_tiempos(tamanos_prueba)
