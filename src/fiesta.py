import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import tkinter as tk
from tkinter import filedialog
from fiesta.resolver import resolver_fiesta

def leer_entrada_desde_archivo(file_path):
    with open(file_path, "r") as f:
        contenido = f.read().strip().split("\n")

    print(f"\n📂 Archivo abierto: {file_path}")
    print("🧾 Contenido leído del archivo:")
    for linea in contenido:
        print("  ", linea)

    idx = 0
    num_problemas = int(contenido[idx])
    idx += 1

    resultados = []

    for problema_num in range(num_problemas):
        m = int(contenido[idx])
        idx += 1
        print(f"\n📌 Problema #{problema_num + 1} con {m} empleados (espera {m} filas + 1 línea de convivencias)")

        matriz = []
        for _ in range(m):
            fila = list(map(int, contenido[idx].split()))
            matriz.append(fila)
            idx += 1

        convivencias = list(map(int, contenido[idx].split()))
        idx += 1

        if len(matriz) != m:
            print(f"⚠️ Advertencia: se esperaban {m} filas pero se leyeron {len(matriz)}")
        if len(convivencias) != m:
            print(f"⚠️ Advertencia: se esperaban {m} valores de convivencia pero se leyeron {len(convivencias)}")

        soluciones = resolver_fiesta(matriz, convivencias)

        for metodo, (resultado, tiempo) in soluciones.items():
            if resultado is None:
                resultado_linea = f"{metodo.upper()}: NO EJECUTADO"
            else:
                invitados, suma = resultado
                resultado_linea = f"{metodo.upper()}: " + " ".join(map(str, invitados)) + f" {suma}"
            resultados.append(resultado_linea)



        resultados.append("")  # Línea vacía entre problemas

    return resultados

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt *.in"), ("Todos los archivos", "*.*")]
    )

    if not file_path:
        print("No se seleccionó ningún archivo.")
        return

    resultados = leer_entrada_desde_archivo(file_path)

    print("\n--- RESULTADOS ---")
    for linea in resultados:
        print(linea)

if __name__ == "__main__":
    main()
