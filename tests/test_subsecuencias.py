import unittest
import time
import os
import sys

# Agrega la carpeta src al path para poder importar subsecuencias
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from subsecuencias import normalizar, subsecuencia_palindromica_mas_larga

class TestPalindromosJuguete(unittest.TestCase):

    def setUp(self):
        # Ruta relativa al archivo de entrada
        ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'subsecuencias.txt')

        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        self.cantidad = int(lineas[0].strip())
        self.entradas = [linea.strip() for linea in lineas[1:self.cantidad + 1]]

        # Resultados esperados (deben coincidir con las entradas del archivo)
        self.esperados = [
            "anitalavalatina",
            "dabalearrozalazorraelabad",
        
        ]

    def test_palindromos_juguete(self):
        repeticiones = 5
        tiempos = []

        for _ in range(repeticiones):
            inicio = time.time()

            for i in range(self.cantidad):
                normalizada = normalizar(self.entradas[i])
                resultado = subsecuencia_palindromica_mas_larga(normalizada)
                self.assertEqual(resultado, self.esperados[i])

            fin = time.time()
            tiempos.append(fin - inicio)

        tiempo_promedio = sum(tiempos) / repeticiones
        print(f"\n[PRUEBA JUGUETE] Tiempo promedio en {repeticiones} repeticiones: {tiempo_promedio:.5f} segundos")

if __name__ == '__main__':
    unittest.main()

