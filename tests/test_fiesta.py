import unittest
from src.fiesta.fuerza_bruta import resolver_fiesta_fuerza_bruta
from src.fiesta.voraz import resolver_fiesta_voraz
from src.fiesta.resolver import resolver_fiesta

class TestFiesta(unittest.TestCase):
     # --- GRAFOS DIRIGIDOS CON CICLOS (estrategia fuerza bruta) ---
    def test_01_ejemplo_con_ciclo(self):
        matriz = [
            [0, 1, 0, 0, 0],  # A → B
            [0, 0, 1, 0, 0],  # B → C
            [0, 0, 0, 1, 0],  # C → D
            [0, 0, 0, 0, 1],  # D → E
            [1, 0, 0, 0, 0],  # E → A (ciclo cerrado)
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta_fuerza_bruta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)

    def test_02_caso_con_6_empleados_y_ciclos(self):
        matriz = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0]
        ]
        convivencias = [12, 21, 5, 10, 8, 7]
        invitados, suma = resolver_fiesta_fuerza_bruta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1, 0])
        self.assertEqual(suma, 29)
    # --- GRAFOS DIRIGIDOS CON CICLOS (estrategia voraz) ---
    def test_03_ejemplo_con_ciclo(self):
        matriz = [
            [0, 1, 0, 0, 0],  # A → B
            [0, 0, 1, 0, 0],  # B → C
            [0, 0, 0, 1, 0],  # C → D
            [0, 0, 0, 0, 1],  # D → E
            [1, 0, 0, 0, 0],  # E → A (ciclo cerrado)
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)

    def test_04_caso_con_6_empleados_y_ciclos(self):
        matriz = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0]
        ]
        convivencias = [12, 21, 5, 10, 8, 7]
        invitados, suma = resolver_fiesta(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1, 0])
        self.assertEqual(suma, 29)

    # --- ÁRBOLES (detección automática y DP) ---
    def test_05_arbol_5_empleados(self):
        matriz = [
            [0, 1, 0, 0, 0],  # 0 supervisa a 1
            [0, 0, 1, 0, 0],  # 1 supervisa a 2
            [0, 0, 0, 1, 0],  # 2 supervisa a 3
            [0, 0, 0, 0, 1],  # 3 supervisa a 4
            [0, 0, 0, 0, 0],  # 4 no supervisa a nadie
        ]
        convivencias = [10, 30, 15, 5, 8]
        invitados, suma = resolver_fiesta(matriz, convivencias)
        self.assertEqual(suma, 38)
        self._verificar_restricciones(matriz, invitados)

    def test_06_arbol_6_empleados(self):
        matriz = [
            [0, 1, 1, 0, 0, 0],  # 0 supervisa a 1 y 2
            [0, 0, 0, 1, 0, 0],  # 1 supervisa a 3
            [0, 0, 0, 0, 1, 1],  # 2 supervisa a 4 y 5
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        convivencias = [5, 6, 7, 8, 9, 10]
        invitados, suma = resolver_fiesta(matriz, convivencias)
        self.assertEqual(suma, 32)
        self._verificar_restricciones(matriz, invitados)

    # --- Caso con autorreferencia ---
    def test_07_empleado_se_supervisa_a_si_mismo(self):
        matriz = [
            [1, 1, 0],  # 0 se supervisa y supervisa a 1
            [0, 0, 1],  # 1 supervisa a 2
            [0, 0, 0],  # 2 no supervisa
        ]
        convivencias = [100, 20, 30]
        invitados, suma = resolver_fiesta(matriz, convivencias)
        self.assertEqual(suma, 30)
        self.assertEqual(invitados, [0, 0, 1])  # Solo el 2 es válido

    # --- Validación general de restricciones ---
    def _verificar_restricciones(self, matriz, invitados):
        n = len(matriz)
        for i in range(n):
            if invitados[i]:
                self.assertEqual(matriz[i][i], 0, f"{i} se supervisa a sí mismo")
                for j in range(n):
                    if i != j and invitados[j]:
                        self.assertEqual(matriz[i][j], 0, f"{i} supervisa a {j}")
                        self.assertEqual(matriz[j][i], 0, f"{j} supervisa a {i}")

if __name__ == "__main__":
    unittest.main()
