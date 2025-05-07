import matplotlib.pyplot as plt
import random
import time

from src.fiesta.dp_arbol import resolver_fiesta_dp_arbol
from src.fiesta.voraz import resolver_fiesta_voraz

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

    for n in tamanos:
        print(f"\n⏱ Tamaño {n}: ", end="")
        tiempos_n_dp = []
        tiempos_n_voraz = []

        for _ in range(repeticiones):
            matriz = generar_arbol_enraizado(n)
            convivencias = generar_convivencias(n)

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
        print(f"Voraz {promedio_voraz:.4f}s, DP {promedio_dp:.4f}s")

        tiempos_dp.append(promedio_dp)
        tiempos_voraz.append(promedio_voraz)

    # Curvas teóricas ajustadas visualmente
    valores_teoricos_dp = [n * 1e-6 for n in tamanos]           # O(n)
    valores_teoricos_voraz = [n**2 * 1e-8 for n in tamanos]     # O(n²)

    plt.plot(tamanos, tiempos_dp, label="DP Árbol (experimental)", marker='o')
    plt.plot(tamanos, tiempos_voraz, label="Voraz (experimental)", marker='x')
    plt.plot(tamanos, valores_teoricos_dp, '--', label="DP O(n) teórico")
    plt.plot(tamanos, valores_teoricos_voraz, '--', label="Voraz O(n²) teórico")

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos vs complejidad teórica")
    plt.legend()
    plt.grid(True)

    plt.savefig("docs/imagenes/tiempos_vs_complejidad.png")
    plt.show()

if __name__ == "__main__":
    tamanos_prueba = [100, 500, 1000, 2000, 5000, 10000, 15000, 20000]
    medir_y_graficar_tiempos(tamanos_prueba)
