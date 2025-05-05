# --- VORAZ ---
# Algoritmo voraz para resolver el problema de la fiesta
def resolver_fiesta_voraz(matriz, convivencias):
    n = len(matriz)
    empleados = list(range(n))

    # Ordenar empleados por su convivencia (de mayor a menor)
    empleados.sort(key=lambda i: convivencias[i], reverse=True)

    invitados = []
    invitados_set = set()

    for i in empleados:
        puede_invitarse = True
        for j in invitados_set:
            if matriz[i][j] == 1 or matriz[j][i] == 1:
                puede_invitarse = False
                break
        if puede_invitarse:
            invitados.append(i)
            invitados_set.add(i)

    # Generar lista de 1s y 0s
    seleccion = [1 if i in invitados_set else 0 for i in range(n)]
    suma = sum(convivencias[i] for i in invitados)
    return seleccion, suma
