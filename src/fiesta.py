# main_fiesta.py

import tkinter as tk
from tkinter import filedialog
from fiesta.resolver import resolver_fiesta  # Ajusta si tu función está en otro archivo

def leer_entrada_desde_archivo(file_path):
    with open(file_path, "r") as f:
        contenido = f.read().strip().split("\n")

    idx = 0
    num_problemas = int(contenido[idx])
    idx += 1

    resultados = []

    for _ in range(num_problemas):
        m = int(contenido[idx])
        idx += 1

        matriz = []
        for _ in range(m):
            fila = list(map(int, contenido[idx].split()))
            matriz.append(fila)
            idx += 1

        convivencias = list(map(int, contenido[idx].split()))
        idx += 1

        invitados, suma = resolver_fiesta(matriz, convivencias)
        resultado_linea = " ".join(map(str, invitados)) + f" {suma}"
        resultados.append(resultado_linea)

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
