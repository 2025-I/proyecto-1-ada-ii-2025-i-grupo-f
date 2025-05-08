import tkinter as tk
from tkinter import filedialog
import time
import re

# Función para normalizar la cadena (eliminar caracteres no alfanuméricos y convertir a minúsculas)
def normalizar(cadena):
    return ''.join(c.lower() for c in cadena if c.isalnum())

# Método 1: Programación Dinámica
def subsecuencia_palindromica_mas_larga_dinamica(s):
    n = len(s)
    if n == 0:
        return ''

    dp = [['' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = s[i]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            if s[i] == s[j]:
                if longitud == 2:
                    dp[i][j] = s[i] + s[j]
                else:
                    dp[i][j] = s[i] + dp[i + 1][j - 1] + s[j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], key=len)

    return dp[0][n - 1]

# Método 2: Fuerza Bruta
def subsecuencia_palindromica_mas_larga_fuerza_bruta(s):
    n = len(s)
    max_palindrome = ''
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subseq = s[i:j]
            if subseq == subseq[::-1] and len(subseq) > len(max_palindrome):
                max_palindrome = subseq
    
    return max_palindrome

# Método 3: Voraz (Greedy)
def subsecuencia_palindromica_mas_larga_voraz(s):
    i, j = 0, len(s) - 1
    resultado = []

    while i <= j:
        if s[i] == s[j]:
            resultado.append(s[i])
            i += 1
            j -= 1
        elif s[i] != s[j]:
            # Elegimos avanzar el puntero que está más lejos de encontrar un match
            # (heurística simple: ignorar el carácter que menos probablemente forme parte del palíndromo)
            if s.count(s[i]) < s.count(s[j]):
                i += 1
            else:
                j -= 1

    mitad = ''.join(resultado)
    # Si hay un centro duplicado, lo agregamos invertido excepto si ya estamos en el medio
    if i - j == 2:
        return mitad + mitad[::-1]
    else:
        return mitad + mitad[-2::-1]
    
# Función para abrir un selector de archivos y leer el archivo seleccionado
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
    return archivo

# Leer el archivo y procesar las cadenas
def leer_cadenas_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        cantidad = int(lineas[0].strip())  # La primera línea es el número de cadenas
        cadenas = [linea.strip() for linea in lineas[1:cantidad+1]]
        return cadenas

def procesar_archivo(ruta_archivo):
    cadenas = leer_cadenas_desde_archivo(ruta_archivo)
    for cadena in cadenas:
        normalizada = normalizar(cadena)
        resultado_dinamica = subsecuencia_palindromica_mas_larga_dinamica(normalizada)
        resultado_fuerza_bruta = subsecuencia_palindromica_mas_larga_fuerza_bruta(normalizada)
        resultado_voraz = subsecuencia_palindromica_mas_larga_voraz(normalizada)
        
        print(f"Dinamica: {resultado_dinamica}")
        print(f"Fuerza Bruta: {resultado_fuerza_bruta}")
        print(f"Voraz: {resultado_voraz}")

if __name__ == "__main__":
    archivo = seleccionar_archivo()  # Abrir el selector de archivos
    if archivo:  # Si se seleccionó un archivo
        procesar_archivo(archivo)
    else:
        print("No se seleccionó ningún archivo.")

