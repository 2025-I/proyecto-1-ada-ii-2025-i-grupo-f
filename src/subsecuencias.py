# src/subsecuencias.py
def encontrar_subsecuencia(lista, subsecuencia):
    n = len(subsecuencia)
    for i in range(len(lista) - n + 1):
        if lista[i:i + n] == subsecuencia:
            return True
    return False