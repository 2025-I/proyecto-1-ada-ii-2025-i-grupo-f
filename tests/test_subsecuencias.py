import unittest
import random
import string
import time

from src.subsecuencias import (
    normalizar,
    subsecuencia_palindromica_mas_larga_dinamica,
    subsecuencia_palindromica_mas_larga_fuerza_bruta,
    subsecuencia_palindromica_mas_larga_voraz
)

def generar_cadena_aleatoria(n):
    letras = string.ascii_letters + string.digits
    return ''.join(random.choice(letras) for _ in range(n))

class TestSubsecuenciasRendimiento(unittest.TestCase):

    def test_subsecuencias_rendimiento(self):
        tamanos = [
            ("juguete", 10),
            ("pequeño", 100),
            ("mediano", 1000),
            ("grande", 10000),
            # ("extra_grande", 20000),  # Descomenta si tu PC lo permite
        ]
        repeticiones = 3

        for nombre, n in tamanos:
            print(f"\n🧪 Tamaño: {nombre} (n={n})")
            cadena = generar_cadena_aleatoria(n)
            cadena_normalizada = normalizar(cadena)

            if n <= 20:
                tiempos_fb = []
                for _ in range(repeticiones):
                    t0 = time.perf_counter()
                    subsecuencia_palindromica_mas_larga_fuerza_bruta(cadena_normalizada)
                    t1 = time.perf_counter()
                    tiempos_fb.append(t1 - t0)
                print(f"🧪 Fuerza Bruta: {sum(tiempos_fb)/repeticiones:.6f}s")

            tiempos_dinamica = []
            for _ in range(repeticiones):
                t0 = time.perf_counter()
                subsecuencia_palindromica_mas_larga_dinamica(cadena_normalizada)
                t1 = time.perf_counter()
                tiempos_dinamica.append(t1 - t0)
            print(f"📘 Dinámica: {sum(tiempos_dinamica)/repeticiones:.6f}s")

            tiempos_voraz = []
            for _ in range(repeticiones):
                t0 = time.perf_counter()
                subsecuencia_palindromica_mas_larga_voraz(cadena_normalizada)
                t1 = time.perf_counter()
                tiempos_voraz.append(t1 - t0)
            print(f"⚙️  Voraz: {sum(tiempos_voraz)/repeticiones:.6f}s")

if __name__ == "__main__":
    unittest.main()
