import tkinter as tk
from tkinter import filedialog


def normalizar(s):
    return ''.join(c.lower() for c in s if c.isalnum())


def subsecuencia_palindromica_mas_larga_dinamica(s):
    normalized = normalizar(s)
    n = len(normalized)
    if n == 0:
        return ""

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    start = 0
    max_length = 1

    for i in range(n - 1):
        if normalized[i] == normalized[i + 1]:
            dp[i][i + 1] = 2
            start = i
            max_length = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if normalized[i] == normalized[j] and dp[i + 1][j - 1] > 0:
                dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    start = i

    result = ""
    i, j = start, start + max_length - 1
    while i <= j:
        if i == j:
            result += normalized[i]
            break
        elif normalized[i] == normalized[j]:
            result += normalized[i]
            i += 1
            j -= 1
        else:
            if dp[i + 1][j] > dp[i][j - 1]:
                i += 1
            else:
                j -= 1

    if max_length > 1:
        if max_length % 2 == 0:
            result = result + result[::-1]
        else:
            result = result + result[:-1][::-1]

    return result


def subsecuencia_palindromica_mas_larga_fuerza_bruta(s):
    normalized = normalizar(s)
    n = len(normalized)
    max_palindromic_subsequence = ""

    def generate(index, current):
        nonlocal max_palindromic_subsequence
        if index == n:
            if current == current[::-1] and len(current) > len(max_palindromic_subsequence):
                max_palindromic_subsequence = current
            return
        generate(index + 1, current + normalized[index])
        generate(index + 1, current)

    if n <= 15:
        generate(0, "")
        return max_palindromic_subsequence
    else:
        return subsecuencia_palindromica_mas_larga_dinamica(s)


def subsecuencia_palindromica_mas_larga_voraz(s):
    """
    Busca subcadenas palindrómicas de forma expansiva desde el centro.
    No es adecuado para subsecuencias separadas.
    """
    normalized = normalizar(s)
    n = len(normalized)
    best_palindrome = ""

    def expand(center_left, center_right):
        while center_left >= 0 and center_right < n and normalized[center_left] == normalized[center_right]:
            center_left -= 1
            center_right += 1
        return normalized[center_left + 1:center_right]

    for i in range(n):
        # Impares
        p1 = expand(i, i)
        # Pares
        p2 = expand(i, i + 1)
        best_palindrome = max(best_palindrome, p1, p2, key=len)

    return best_palindrome


def process_input_file(file_content):
    lines = file_content.strip().split('\n')
    n = int(lines[0])
    results = []

    for i in range(1, n + 1):
        cadena = lines[i]
        dp_res = subsecuencia_palindromica_mas_larga_dinamica(cadena)
        fb_res = subsecuencia_palindromica_mas_larga_fuerza_bruta(cadena)
        gz_res = subsecuencia_palindromica_mas_larga_voraz(cadena)
        results.append((dp_res, fb_res, gz_res))

    return results


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    if not archivo:
        print("No se seleccionó ningún archivo.")
        exit()

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    resultados = process_input_file(contenido)

    for idx, (dp, fb, gz) in enumerate(resultados, 1):
        print(f"Cadena {idx}:")
        print(f"  DP: {dp}")
        print(f"  FB: {fb}")
        print(f"  GZ: {gz}")
        print()
