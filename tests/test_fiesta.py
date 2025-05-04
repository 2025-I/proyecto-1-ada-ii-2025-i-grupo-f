import unittest
import sys
import os


from src.fiesta import resolver_fiesta

class TestResolverFiesta(unittest.TestCase):

    def test_ejemplo_oficial_1(self):
        m = 5
        matriz = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0]
        ]
        calificaciones = [10, 30, 15, 5, 8]
        invitados, total = resolver_fiesta(m, matriz, calificaciones)
        self.assertEqual(invitados, [0, 1, 0, 1, 0])
        self.assertEqual(total, 35)

    def test_ejemplo_oficial_2(self):
        m = 6
        matriz = [
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0]
        ]
        calificaciones = [12, 21, 5, 10, 8, 7]
        invitados, total = resolver_fiesta(m, matriz, calificaciones)
        self.assertEqual(invitados, [1, 0, 0, 0, 0, 1])
        self.assertEqual(total, 19)

if __name__ == "__main__":
    unittest.main()
