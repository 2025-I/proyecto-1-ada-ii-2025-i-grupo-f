[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kKWtV-CB)
# Proyecto #1: Análisis de Algoritmos II
 
**Profesor:** Carlos Andrés Delgado S.  
**Fecha:** Mayo 7 2025  
**Estudiantes:**  
- Johan Acosta  - 2380393
- Juan Camilo Gutiérrez - 2159874 
- Andrés Felipe Rojas - 2160328

---

## 🎯 Descripción del problema

Dado un árbol que representa la jerarquía de empleados de una empresa y sus calificaciones de convivencia, el objetivo es maximizar la suma de dichas calificaciones al seleccionar un subconjunto de empleados para asistir a una fiesta. **Restricción:** ningún empleado puede asistir si su supervisor directo también lo hace.

---

## 🧠 Enfoques implementados

Se implementaron tres estrategias para resolver el problema:

- **Fuerza bruta** (exploración exhaustiva)
- **Voraz** (selección localmente óptima)
- **Programación dinámica sobre árboles**

---

## 🗂️ Estructura de carpetas


---


---

## 📄 Descripción de los archivos

### `fiesta.py`
Archivo principal de entrada. Permite al usuario seleccionar un archivo `.txt` con los datos de entrada. Procesa todos los problemas y ejecuta los tres métodos, mostrando los resultados en consola.

![fiesta](docs/imagenes/imagen1.png)
![fiesta](docs/imagenes/imagen1-1.png)

---

### `resolver.py`
Controlador principal que llama a cada una de las estrategias y mide su tiempo de ejecución.

![resolver](docs/imagenes/imagen2.png)

---

### `dp_arbol.py`
Implementación basada en **programación dinámica sobre árboles**. Usa recursividad y decisiones óptimas para cada nodo.

![dp arbol](docs/imagenes/imagen3.png)
![dp arbol](docs/imagenes/imagen3-1.png)

---

### `fuerza_bruta.py`
Explora todas las combinaciones posibles de empleados y selecciona la de mayor suma válida.

![fuerza bruta](docs/imagenes/imagen4.png)

---

### `voraz.py`
Selecciona empleados por orden descendente de calificación, evitando conflictos con invitados anteriores.

![voraz](docs/imagenes/imagen5.png)

---

### `utils.py`
Contiene funciones auxiliares para:
- Convertir la matriz de adyacencia a lista
- Validar si la estructura es un árbol enraizado

![utils](docs/imagenes/imagen6.png)
![utils](docs/imagenes/imagen6-1.png)

---

### `medir_tiempo.py`
Script para medir rendimiento de los métodos **DP** y **Voraz** con entradas generadas aleatoriamente. Genera gráficas comparando la complejidad teórica con los resultados experimentales.

![medir](docs/imagenes/imagen7.jpeg)

---

## ✅ Pruebas (Problema 2)

Se realizaron pruebas unitarias usando `unittest`, en el archivo `test_subsecuencias.py`. Las pruebas del problema 2 pueden integrarse siguiendo la misma lógica, validando que:

- Las soluciones generadas por cada método respetan la restricción jerárquica.
- La suma total corresponde a la de los empleados invitados.
- Se evalúan con diferentes tamaños (juguete, pequeño, etc.)

📸 *Colocar captura del uso de `assertEqual` en el archivo de prueba para `subsecuencia_palindromica_mas_larga` (aunque este es del problema 1, sirve de ejemplo de cómo estructurar para el problema 2)*

---

## 🧪 Tiempos de ejecución

Los tiempos fueron medidos con `time.perf_counter()` y promediados en 5 ejecuciones para los siguientes tamaños:

- 100, 500, 1000, 2000, 5000, 10000, 15000, 20000

📸 *Colocar fragmento de código donde se miden los tiempos (`medir_tiempo.py` líneas 17 a 34)*

📸 *Colocar gráfica generada con `matplotlib`*

---

## 🛠️ Requisitos técnicos

- Estructura de proyecto modular
- Lectura de archivo con selector gráfico (`tkinter`)
- Pruebas con `unittest`
- Uso de Git y GitHub Actions para CI/CD
- Informe en Markdown

---

## 📈 Complejidad computacional estimada

| Método         | Complejidad estimada |
|----------------|----------------------|
| Fuerza bruta   | O(2ⁿ × n²)            |
| Voraz          | O(n²)                |
| DP en árbol    | O(n)                 |

---

## 📄 Problema 1: Subsecuencias más largas de un palíndromo

Se implementaron tres métodos para encontrar la subsecuencia palindrómica más larga en una cadena:

- **Fuerza bruta:** explora todas las posibles subsecuencias.
- **Programación dinámica:** utiliza subproblemas para construir la solución óptima.
- **Voraz (pseudo-voraz):** detecta palíndromos al expandir desde el centro (más eficiente en tiempo real, pero no siempre da la subsecuencia más larga si no es continua).

### `subsecuencias.py`

Este archivo contiene los tres métodos, más una función de normalización y lectura desde archivo usando `filedialog`.

![normalizar](docs/imagenes/imagen8.png)
![dinamica](docs/imagenes/imagen8-1.png)
![fuerza bruta](docs/imagenes/imagen8-2.png)
![voraz](docs/imagenes/imagen8-3.png)
![procesar archivo](docs/imagenes/imagen8-4.png)

---

## ✅ Pruebas (Problema 1)

El archivo `test/test_subsecuencias.py` contiene pruebas automatizadas para verificar el rendimiento y la correctitud de los tres métodos. Las pruebas incluyen tamaños:

- **Juguete** (10)
- **Pequeño** (100)
- **Mediano** (1000)
- **Grande** (10000)
- *(Extra grande comentado por precaución)*

![test sub](docs/imagenes/imagen9.png)
![test sub](docs/imagenes/imagen9-1.png)

---

## 📈 Complejidad estimada (Problema 1)

| Método                         | Complejidad          |
|-------------------------------|----------------------|
| Fuerza bruta                  | O(n³)                |
| Programación dinámica         | O(n²)                |
| Búsqueda centro-expandida     | O(n²)                |

---

## 🧾 Conclusiones

- La programación dinámica es la más confiable para obtener la solución óptima, especialmente para cadenas largas.
- La estrategia voraz (center-expansion) es muy rápida, pero puede fallar si la subsecuencia palindrómica más larga no es continua.
- La fuerza bruta es solo viable en tamaños muy pequeños, útil como benchmark o para validación.

