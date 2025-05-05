# --- Método Voraz para grafos generales (ciclos permitidos) ---
def resolver_fiesta_voraz(matriz, convivencias):
    n = len(matriz) #cantidad de empleados 
    empleados = list(range(n)) #Crea una lista con los índices de todos los empleados: [0, 1, 2, ..., n-1].
    # Paso 1: Crear listas para registrar supervisiones
    supervisa = [set() for _ in range(n)]   #  empleados que son supervisados por i
    supervisado_por = [set() for _ in range(n)] # quién supervisa a j
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j]==1:
                supervisa[i].add(j) #Se agrega j al conjunto supervisa[i].
                supervisado_por[j].add(i) #Se agrega i al conjunto supervisado_por[j].

    # Paso 2: Ordenar empleados por mayor convivencia (descendente)
    #
    empleados.sort(key=lambda x: convivencias[x], reverse=True)
    # Paso 3: Seleccionar invitados evitando conflictos
    invitados = [0] * n #5 → [0, 0, 0, 0, 0]
    incompatibles = set() # los que no pueden ser invitados

    for i in empleados: 
        if i in incompatibles:
            continue
        if matriz[i][i] == 1:  # se supervisa a sí mismo
            continue
        invitados[i] = 1

        # Marcar como incompatibles a quienes él supervisa o lo supervisan
        incompatibles.update(supervisa[i])
        incompatibles.update(supervisado_por[i])
        incompatibles.add(i)
     # Paso 4: Calcular la suma de convivencia de los invitados
    suma = sum(convivencias[i] for i in range(n) if invitados[i])

    return invitados, suma