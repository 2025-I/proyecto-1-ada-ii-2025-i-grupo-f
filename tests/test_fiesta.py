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
     ###pequeño arbol   
    def test_03_arbol_pequeno(self):
        matriz = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        convivencias = [10, 20, 30, 15, 25, 5, 10, 18, 12, 7]

        invitados, suma = resolver_fiesta_fuerza_bruta(matriz, convivencias)

        # Óptimo: invitar a nodos 0, 2, 4, 6, 8 (índices pares)
        self.assertEqual(invitados, [1, 0, 1, 0, 1, 0, 0, 1, 0, 1])
        self.assertEqual(suma, 90)
    # --- estrategia voraz ---
    def test_04_ejemplo_5(self):
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
       
    def test_05_caso_con_6(self):
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
     ###pequeño arbol   
    def test_06_arbol_pequeno(self):
        matriz = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        convivencias = [10, 20, 30, 15, 25, 5, 10, 18, 12, 7]

        invitados, suma = resolver_fiesta_voraz(matriz, convivencias)

        # Óptimo: invitar a nodos 0, 2, 4, 6, 8 (índices pares)
        self.assertEqual(invitados, [1, 0, 1, 0, 1, 0, 0, 1, 0, 1])
        self.assertEqual(suma, 90)

    # ---   DP ---
    def test_07_ejemplo_con_5(self):
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
        
    def test_08_caso_con_6(self):
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

     ###pequeño arbol   
    def test_09_arbol_pequeno(self):
        matriz = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        convivencias = [10, 20, 30, 15, 25, 5, 10, 18, 12, 7]

        invitados, suma = resolver_fiesta_dp_arbol(matriz, convivencias)

        # Óptimo: invitar a nodos 0, 2, 4, 6, 8 (índices pares)
        self.assertEqual(invitados, [1, 0, 1, 0, 1, 0, 0, 1, 0, 1])
        self.assertEqual(suma, 90)
    # --- Caso con autorreferencia ---
    # --- Validación de solución ---
    def _es_solucion_valida(self, matriz, invitados):
        n = len(invitados)
        for i in range(n):
            if invitados[i]:  # Si el empleado i fue invitado
                for j in range(n):
                    if invitados[j] and matriz[i][j] == 1:
                        print(f"❌ Conflicto: el invitado {i} supervisa al invitado {j}")
                        return False
        return True


    def test_rendimiento_por_tamano(self):
        tamanos = [
            ("juguete", 10),
            ("pequeño", 100),
            ("mediano", 1000),
            ("grande", 10000),
        ]
        repeticiones = 1

        for nombre, n in tamanos:
            print(f"\n⏳ Tamaño: {nombre} (n={n})")

            for _ in range(repeticiones):
                m = generar_arbol_enraizado(n)
                c = generar_convivencias(n)

                if n <= 20:
                    t0 = perf_counter()
                    invitados_fb, suma_fb = resolver_fiesta_fuerza_bruta(m, c)
                    t1 = perf_counter()
                    self.assertTrue(self._es_solucion_valida(m, invitados_fb), f"❌ Fuerza Bruta inválida en n={n}")
                    print(f"🧪 Fuerza Bruta: suma={suma_fb}, tiempo={t1 - t0:.6f}s")

                t0 = perf_counter()
                invitados_vz, suma_vz = resolver_fiesta_voraz(m, c)
                t1 = perf_counter()
                self.assertTrue(self._es_solucion_valida(m, invitados_vz), f"❌ Voraz inválida en n={n}")
                print(f"⚙️  Voraz: suma={suma_vz}, tiempo={t1 - t0:.6f}s")

                t0 = perf_counter()
                invitados_dp, suma_dp = resolver_fiesta_dp_arbol(m, c)
                t1 = perf_counter()
                self.assertTrue(self._es_solucion_valida(m, invitados_dp), f"❌ DP inválida en n={n}")
                print(f"📘 DP Árbol: suma={suma_dp}, tiempo={t1 - t0:.6f}s")

if __name__ == "__main__":
    unittest.main()
