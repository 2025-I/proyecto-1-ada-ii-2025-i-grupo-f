import unittest
from src.fiesta.fuerza_bruta import resolver_fiesta_fuerza_bruta
from src.fiesta.voraz import resolver_fiesta_voraz
from src.fiesta.dp_arbol import resolver_fiesta_dp_arbol

class TestFiesta(unittest.TestCase):
     # --- estrategia fuerza bruta---
    def test_01_ejemplo_con_ciclo(self):
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

    def test_02_caso_con_6_empleados_y_ciclos(self):
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
    def test_03_ejemplo_con_ciclo(self):
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

    def test_04_caso_con_6_empleados_y_ciclos(self):
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
    def test_05_ejemplo_con_ciclo(self):
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

    def test_06_caso_con_6_empleados_y_ciclos(self):
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
   

    # --- Validación general de restricciones ---
    def _verificar_restricciones(self, matriz, invitados):
        n = len(matriz)
        for i in range(n):
            if invitados[i]:
                for j in range(n):
                    if i != j and invitados[j]:
                        self.assertEqual(matriz[i][j], 0, f"{i} supervisa a {j}")
                        self.assertEqual(matriz[j][i], 0, f"{j} supervisa a {i}")


if __name__ == "__main__":
    unittest.main()
