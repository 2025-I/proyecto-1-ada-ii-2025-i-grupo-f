import matplotlib.pyplot as plt
import random
import string
import time

from subsecuencias import (
    subsecuencia_palindromica_mas_larga_dinamica,
    subsecuencia_palindromica_mas_larga_fuerza_bruta,
    subsecuencia_palindromica_mas_larga_voraz
)

def generar_cadena_aleatoria(longitud):
    return ''.join(random.choices(string.ascii_lowercase, k=longitud))

def medir_tiempos(cantidades, repeticiones=3):
    tiempos_dp = []
    tiempos_fb = []
    tiempos_vz = []

    for n in cantidades:
        print(f"Tamaño {n}:", end=" ")
        cadenas = [generar_cadena_aleatoria(n) for _ in range(repeticiones)]

        t_dp = t_fb = t_vz = 0
        for s in cadenas:
            t0 = time.perf_counter()
            subsecuencia_palindromica_mas_larga_dinamica(s)
            t_dp += time.perf_counter() - t0

            if n <= 20:  # fuerza bruta solo para tamaños pequeños
                t0 = time.perf_counter()
                subsecuencia_palindromica_mas_larga_fuerza_bruta(s)
                t_fb += time.perf_counter() - t0

            t0 = time.perf_counter()
            subsecuencia_palindromica_mas_larga_voraz(s)
            t_vz += time.perf_counter() - t0

        tiempos_dp.append(t_dp / repeticiones)
        tiempos_fb.append((t_fb / repeticiones) if n <= 20 else None)
        tiempos_vz.append(t_vz / repeticiones)
        print(f"DP={tiempos_dp[-1]:.4f}s, Voraz={tiempos_vz[-1]:.4f}s", end="")
        if n <= 20:
            print(f", Fuerza Bruta={tiempos_fb[-1]:.4f}s")
        else:
            print("")

    return tiempos_dp, tiempos_fb, tiempos_vz

def graficar(cantidades, tiempos_dp, tiempos_fb, tiempos_vz):
    plt.plot(cantidades, tiempos_dp, label="DP (experimental)", marker='o')
    plt.plot(cantidades, tiempos_vz, label="Voraz (experimental)", marker='x')

    if any(tiempos_fb):
        x_fb = [n for n, t in zip(cantidades, tiempos_fb) if t is not None]
        y_fb = [t for t in tiempos_fb if t is not None]
        plt.plot(x_fb, y_fb, label="Fuerza Bruta (experimental)", marker='s')

    # Curvas teóricas para comparación visual
    teorico_dp = [n**2 * 1e-7 for n in cantidades]
    teorico_voraz = [n**2 * 2e-7 for n in cantidades]
    teorico_fb = [n**3 * 1e-9 if n <= 20 else None for n in cantidades]

    plt.plot(cantidades, teorico_dp, '--', label="DP teórico O(n²)")
    plt.plot(cantidades, teorico_voraz, '--', label="Voraz teórico O(n²)")

    if any(teorico_fb):
        x_fb = [n for n, t in zip(cantidades, teorico_fb) if t is not None]
        y_fb = [t for t in teorico_fb if t is not None]
        plt.plot(x_fb, y_fb, '--', label="Fuerza Bruta teórica O(n³)")

    plt.xlabel("Longitud de la cadena")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos de subsecuencia palindrómica")
    plt.legend()
    plt.grid(True)

    import os
    os.makedirs("docs/imagenes", exist_ok=True)
    plt.savefig("docs/imagenes/palindromos_tiempos.png")
    plt.show()

if __name__ == "__main__":
    cantidades = [5, 10, 20, 50, 100, 200, 400, 600, 800, 1000]
    tiempos_dp, tiempos_fb, tiempos_vz = medir_tiempos(cantidades)
    graficar(cantidades, tiempos_dp, tiempos_fb, tiempos_vz)
