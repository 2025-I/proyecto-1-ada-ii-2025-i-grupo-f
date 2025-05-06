import unittest
import random

from src.fiesta.fuerza_bruta import resolver_fiesta_fuerza_bruta
from src.fiesta.voraz import resolver_fiesta_voraz
from src.fiesta.dp_arbol import resolver_fiesta_dp_arbol
from time import perf_counter

# ⬅⬅⬅ Esto va arriba del todo (fuera de la clase)
def generar_arbol_enraizado(n):
    matriz = [[0] * n for _ in range(n)]
    for hijo in range(1, n):
        padre = random.randint(0, hijo - 1)
        matriz[padre][hijo] = 1
    return matriz

def generar_convivencias(n, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]


class TestFiesta(unittest.TestCase):
     # --- estrategia fuerza bruta---
    def test_01_ejemplo_con_5(self):
        matriz = [
            [0, 1, 0, 0, 0],  # A → B
            [0, 0, 1, 0, 0],  # B → C
            [0, 0, 0, 1, 0],  # C → D
            [0, 0, 0, 0, 1],  # D → E
            [0, 0, 0, 0, 0],  # E sin ciclo
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta_fuerza_bruta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)
        

    def test_02_caso_con_6_(self):
        matriz = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        convivencias = [12, 21, 5, 10, 8, 7]
        invitados, suma = resolver_fiesta_fuerza_bruta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 1, 1, 0])
        self.assertEqual(suma, 39)

    # --- estrategia voraz ---
    def test_03_ejemplo_5(self):
        matriz = [
            [0, 1, 0, 0, 0],  # A → B
            [0, 0, 1, 0, 0],  # B → C
            [0, 0, 0, 1, 0],  # C → D
            [0, 0, 0, 0, 1],  # D → E
            [0, 0, 0, 0, 0],  # E sin ciclo
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta_voraz(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)
       
    def test_04_caso_con_6(self):
        matriz = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        convivencias = [12, 21, 5, 10, 8, 7]
        invitados, suma = resolver_fiesta_voraz(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 1, 1, 0])
        self.assertEqual(suma, 39)


    # ---   DP ---
    def test_05_ejemplo_con_5(self):
        matriz = [
            [0, 1, 0, 0, 0],  # A → B
            [0, 0, 1, 0, 0],  # B → C
            [0, 0, 0, 1, 0],  # C → D
            [0, 0, 0, 0, 1],  # D → E
            [0, 0, 0, 0, 0],  # E →sin ciclo
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta_dp_arbol(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)
        
    def test_06_caso_con_6(self):
        matriz = [
            [0, 1, 0, 0, 0, 0], #A SUPERVISA a B
            [0, 0, 1, 1, 0, 0], #B SUPERVISA a C Y D
            [0, 0, 0, 0, 0, 1], #C SUPERVISA a F
            [0, 0, 0, 0, 1, 0], #D SUPERVISA a E      
            [0, 0, 0, 0, 0, 0], #E SUPERVISA a nadie
            [0, 0, 0, 0, 0, 0] #F SUPERVISA a nadie   por lo tanto se lleva a e, f y b
        ]
        convivencias = [12, 18, 5, 10, 8, 7]
        invitados, suma = resolver_fiesta_dp_arbol(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1, 1])
        self.assertEqual(suma, 33)
    # --- Caso con autorreferencia ---
   
    def test_rendimiento_por_tamano(self):
        tamanos = [
            ("juguete", 10),
            ("pequeño", 100),
            ("mediano", 1000),
            ("grande", 10000),
            #("extra_grande", 20000),  # Descomenta si tu PC lo tolera
        ]
        repeticiones = 5

        for nombre, n in tamanos:
            print(f"\n⏳ Tamaño: {nombre} (n={n})")
            
            if n <= 20:
                tiempos_fb = []
                for _ in range(repeticiones):
                    m = generar_arbol_enraizado(n)
                    c = generar_convivencias(n)
                    t0 = perf_counter()
                    resolver_fiesta_fuerza_bruta(m, c)
                    t1 = perf_counter()
                    tiempos_fb.append(t1 - t0)
                print(f"🧪 Fuerza Bruta promedio: {sum(tiempos_fb)/repeticiones:.6f}s")
            if n <= 20000:
                tiempos_vz = []
                for _ in range(repeticiones):
                    m = generar_arbol_enraizado(n)
                    c = generar_convivencias(n)
                    t0 = perf_counter()
                    resolver_fiesta_voraz(m, c)
                    t1 = perf_counter()
                    tiempos_vz.append(t1 - t0)
                print(f"⚙️  Voraz promedio: {sum(tiempos_vz)/repeticiones:.6f}s")

            tiempos_dp = []
            for _ in range(repeticiones):
                m = generar_arbol_enraizado(n)
                c = generar_convivencias(n)
                t0 = perf_counter()
                resolver_fiesta_dp_arbol(m, c)
                t1 = perf_counter()
                tiempos_dp.append(t1 - t0)
            print(f"📘 DP Árbol promedio: {sum(tiempos_dp)/repeticiones:.6f}s")

  

if __name__ == "__main__":
    unittest.main()
