# tests/test_fiesta.py
import unittest
from src.fiesta import leer_entrada, resolver_fiesta_general

class TestFiesta(unittest.TestCase):
    def test_ejemplo_con_ciclo(self):
        entrada = [
            "5",
            "0 1 0 0 0",
            "0 0 1 0 0",
            "0 0 0 1 0",
            "0 0 0 0 1",
            "1 0 0 0 0",
            "10 30 15 5 8"
        ]
        n, matriz, convivencias = leer_entrada(entrada)
        invitados, suma = resolver_fiesta_general(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1])
        self.assertEqual(suma, 38)
    def test_caso_con_6_empleados_y_ciclos(self):
        entrada = [
            "6",
            "0 0 1 0 0 0",
            "1 0 0 0 0 0",
            "0 1 0 0 0 0",
            "0 0 0 1 0 0",
            "0 0 0 0 0 1",
            "1 0 0 0 0 0",
            "12 21 5 10 8 7"
        ]
        n, matriz, convivencias = leer_entrada(entrada)
        invitados, suma = resolver_fiesta_general(matriz, convivencias)
        self.assertEqual(invitados, [0, 1, 0, 0, 1, 0])
        self.assertEqual(suma, 29)
if __name__ == "__main__":
    unittest.main()
