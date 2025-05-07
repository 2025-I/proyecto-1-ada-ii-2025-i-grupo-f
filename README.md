[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kKWtV-CB)
# Proyecto #1: Análisis de Algoritmos II
 
**Profesor:** Carlos Andrés Delgado S.  
**Fecha:** Mayo 7 2025  
**Estudiantes:**  
- Johan Acosta  
- Juan Camilo Gutiérrez  
- Andrés Felipe Rojas

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

## 📄 Descripción de los archivos

### `fiesta.py`
Archivo principal de entrada. Permite al usuario seleccionar un archivo `.txt` con los datos de entrada. Procesa todos los problemas y ejecuta los tres métodos, mostrando los resultados en consola.

![Función DP](docs/imagenes/imagen1.png)

---

### `resolver.py`
Controlador principal que llama a cada una de las estrategias y mide su tiempo de ejecución.

📸 *Colocar captura del diccionario `resultado` y los `print()` de tiempos en `resolver_fiesta()` (líneas 20 a 33).*

---

### `dp_arbol.py`
Implementación basada en **programación dinámica sobre árboles**. Usa recursividad y decisiones óptimas para cada nodo.

📸 *Colocar captura de la función `dp()` interna y el retorno final del arreglo binario (líneas 11 a 44 aprox.)*

---

### `fuerza_bruta.py`
Explora todas las combinaciones posibles de empleados y selecciona la de mayor suma válida.

📸 *Colocar captura de la función `resolver_fiesta_fuerza_bruta()` completa*

---

### `voraz.py`
Selecciona empleados por orden descendente de calificación, evitando conflictos con invitados anteriores.

📸 *Colocar captura de la función `resolver_fiesta_voraz()` completa*

---

### `utils.py`
Contiene funciones auxiliares para:
- Convertir la matriz de adyacencia a lista
- Validar si la estructura es un árbol enraizado

📸 *Colocar captura de la función `es_arbol_enraizado_adj()` completa*

---

### `medir_tiempo.py`
Script para medir rendimiento de los métodos **DP** y **Voraz** con entradas generadas aleatoriamente. Genera gráficas comparando la complejidad teórica con los resultados experimentales.

📸 *Colocar gráfica `tiempos_vs_complejidad.png` generada en `docs/imagenes/`*

---

## ✅ Pruebas

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

## 🧾 Conclusiones

- **DP en árboles** fue el método más eficiente y escalable.
- El **método voraz** es útil para soluciones rápidas, aunque puede no ser óptimo.
- La **fuerza bruta** es inviable para entradas grandes, pero útil para validar correctness.

