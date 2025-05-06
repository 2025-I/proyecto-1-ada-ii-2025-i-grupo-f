import re
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ------------------------------------------
# Función para normalizar una cadena:
# Convierte todos los caracteres a minúsculas
# y elimina cualquier carácter no alfanumérico.
# ------------------------------------------
def normalizar(cadena):
    # re.findall busca todas las letras a-z o dígitos 0-9
    return ''.join(re.findall(r'[a-z0-9]', cadena.lower()))

# ----------------------------------------------------------------
# Función para encontrar la subsecuencia palindrómica más larga.
# Utiliza programación dinámica (DP) para construir una tabla dp.
# dp[i][j] guarda la subsecuencia palindrómica más larga en s[i..j]
# ----------------------------------------------------------------
def subsecuencia_palindromica_mas_larga(s):
    n = len(s)
    
    # Crear una tabla de n x n inicializada con cadenas vacías
    dp = [['' for _ in range(n)] for _ in range(n)]
    
    # Una sola letra es un palíndromo por sí misma
    for i in range(n):
        dp[i][i] = s[i]
    
    # Considerar substrings de longitud 2 hasta n
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1  # Índice final del substring
            
            # Si los caracteres extremos son iguales
            if s[i] == s[j]:
                # Si la longitud es 2, solo concatenamos los dos caracteres
                if longitud == 2:
                    dp[i][j] = s[i] + s[j]
                else:
                    # Caso general: s[i] + solución interna + s[j]
                    dp[i][j] = s[i] + dp[i + 1][j - 1] + s[j]
            else:
                # Si los extremos no coinciden, elegimos la subsecuencia más larga entre dos posibilidades
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], key=len)
    
    # La solución completa está en dp[0][n-1]
    return dp[0][n - 1]

# -----------------------------------------------------
# Función principal que gestiona la lectura de archivo,
# procesamiento de cada línea y medición de tiempo.
# -----------------------------------------------------
def main():
    Tk().withdraw()  # Oculta la ventana principal de Tkinter

    # Abrimos un cuadro de diálogo para que el usuario seleccione un archivo de entrada
    filename = askopenfilename(title="Selecciona el archivo de entrada")

    start_time = time.time()

    # Abrimos el archivo y procesamos línea por línea
    with open(filename, 'r', encoding='utf-8') as file:
        # Leemos la primera línea: cantidad de cadenas a procesar
        n = int(file.readline())
        
        # Procesamos cada una de las n cadenas
        for _ in range(n):
            linea = file.readline().strip()  # Eliminamos espacios extra
            normalizada = normalizar(linea)  # Normalizamos la cadena
            resultado = subsecuencia_palindromica_mas_larga(normalizada)  # Calculamos subsecuencia
            print(resultado)  # Imprimimos el resultado en salida estándar

    
    end_time = time.time()
    
    print(f"Tiempo total de ejecución: {end_time - start_time:.4f} segundos", file=sys.stderr)

if __name__ == "__main__":
    import sys
    main()
