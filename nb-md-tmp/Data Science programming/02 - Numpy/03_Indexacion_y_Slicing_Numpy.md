# 03_Indexacion_y_Slicing_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Indexación, Slicing y Máscaras Booleanas en NumPy 🎯
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/03_Indexacion_y_Slicing_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Indexación, Slicing y Filtrado Booleano en NumPy 🔍

Acceder, recortar y filtrar datos con precisión quirúrgica es la base del análisis exploratorio y la preparación de características:

1. **Indexación y Slicing 1D:** Coordenadas, rangos $[inicio : fin : paso]$ e indexación negativa.
2. **Indexación Multidimensional 2D:** Sintaxis de coma `[fila, columna]` y sub-bloques de matrices.
3. **Fancy Indexing:** Selección no contigua mediante listas o arrays de enteros.
4. **Indexación Booleana (Máscaras Lógicas):** Filtrado condicional sin bucles y la función `np.where()`.

> ⚠️ **Vistas vs Copias en Slicing:** A diferencia de las listas nativas de Python (donde el slicing crea una copia nueva), en NumPy el slicing básico retorna una **vista (*view*)** sobre el mismo bloque de memoria. Modificar una vista modifica el array original.

---
### 1. Indexación Básica y Slicing (1D) 📏

Los arrays unidimensionales (vectores) se comportan de manera idéntica a las listas nativas de Python. 
Utilizan la sintaxis estándar de rebanado (slicing): **`array[inicio : fin : paso]`**

*   **`inicio`**: Desde dónde cortar (incluido).
*   **`fin`**: Hasta dónde cortar (excluido).
*   **`paso`**: De a cuántos elementos saltar.

*Nota: Al igual que en Python, el índice siempre comienza en cero `0`.*

```python
# Configuración interactiva segura
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass
import numpy as np
```

---
#### 🛠️ Práctica 1: Slicing Básico

Crea un array unidimensional que contenga los números del 10 al 20 (incluidos). Extrae y muestra únicamente los últimos 3 elementos usando slicing con índices negativos.

```python
# Escribe tu código aquí

# mi_array = ...
# ultimos_tres = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
mi_array = np.arange(10, 21)
ultimos_tres = mi_array[-3:] # Toma desde el tercero de atrás hacia el final
print(ultimos_tres)
```
</details>

---
### 2. Indexación Multidimensional (Matrices 2D) 🧊

En matrices bidimensionales, la indexación se especifica mediante una tupla separada por coma: `array[filas, columnas]`.

$$\text{matriz}[\text{rango\_filas}, \text{rango\_columnas}]$$

* `matriz[1, 2]`: Elemento en la fila 1, columna 2.
* `matriz[:, 0]`: Primera columna completa (todas las filas).
* `matriz[0, :]`: Primera fila completa (todas las columnas).
* `matriz[1:3, 0:2]`: Sub-matriz de $2 \times 2$ entre las filas 1-2 y columnas 0-1.

```python
# Creamos una matriz de 5 filas y 4 columnas
b = np.array([[ 0,  1,  2,  3],
              [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])

print("Elemento exacto b[2, 3]:", b[2, 3]) # Fila 2, Columna 3

print("\nExtraer toda la SEGUNDA COLUMNA:")
print(b[:, 1]) # El ':' solo significa "tráeme TODAS las filas"

print("\nExtraer un Sub-bloque (Filas 1 a 2, TODAS las columnas):")
print(b[1:3, :])
```

**Iterando sobre Matrices**

Si utilizas un bucle `for` tradicional en una matriz 2D, NumPy recorrerá el primer eje (te entregará fila por fila). Si por alguna razón necesitas iterar absolutamente por cada número individual, NumPy te ofrece el atributo `.flat`.

```python
print("Iterar normal:")
for fila in b:
    print(fila) # Imprime 5 filas

print("\nIterar aplanado con .flat:")
for elemento in list(b.flat)[:6]: # Limitado a los 6 primeros para no llenar la pantalla
    print(elemento)
```

---
#### 🛠️ Práctica 2: Slicing de Matrices

Utilizando la matriz `b` generada arriba:
Extrae un sub-bloque (matriz más pequeña) que contenga únicamente los valores centrales `[11, 12]` y `[21, 22]`.

```python
# Escribe tu código aquí

# sub_bloque = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Filas 1 y 2 (así que cortamos 1:3)
# Columnas 1 y 2 (así que cortamos 1:3)
sub_bloque = b[1:3, 1:3]
print(sub_bloque)
```
</details>

---
### 3. Fancy Indexing (Indexación con Arrays de Enteros) 🎯

**Fancy Indexing** permite pasar una lista o array de enteros para extraer elementos en un orden arbitrario y no contiguo.

> 📌 **Regla de Memoria:** A diferencia del slicing estándar, **Fancy Indexing siempre retorna una COPIA independiente** de los datos en memoria, nunca una vista.

```python
# Creamos un array del 1 al 16, y lo moldeamos a 4x4
arr = np.arange(1, 17).reshape([4, 4])
print("Matriz Original:\n", arr)

# 0  1  2  3
# -----------
# 1  2  3  4   | 0
# 5  6  7  8   | 1
# 9  10 11 12  | 2
# 13 14 15 16  | 3

print("\nExtrayendo la diagonal principal usando Fancy Indexing:")
diagonal = arr[[0, 1, 2, 3], [0, 1, 2, 3]]
print(diagonal)
```

---
#### 🛠️ Práctica 3: Fancy Indexing

Utilizando el mismo array `arr` de 4x4, extrae usando Fancy Indexing los 4 números que están exactamente en las "esquinas" de la matriz (1, 4, 13 y 16).

```python
# Escribe tu código aquí

# esquinas = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Las coordenadas de las esquinas son: [0,0], [0,3], [3,0], [3,3]
# Pasamos todas las X juntas: [0, 0, 3, 3]
# Pasamos todas las Y juntas: [0, 3, 0, 3]
esquinas = arr[[0, 0, 3, 3], [0, 3, 0, 3]]
print(esquinas)
```
</details>

---
### 4. Indexación Booleana y la Función `np.where()` 🎭

La **indexación booleana** aplica condiciones lógicas elemento a elemento para generar una máscara booleana (`True` / `False`) y filtrar únicamente los valores que cumplen la condición.

#### La Función `np.where(condicion, valor_si_true, valor_si_false)`:
* Actúa como un operador ternario vectorizado ultrarrápido para imputar, categorizar o binarizar variables continuas en Data Science.

```python
arr2 = np.arange(1, 17).reshape([4, 4])

# 1. Creamos una condición. ¿Qué números son pares?
mascara = (arr2 % 2 == 0)
print("Máscara Booleana (True = Par):\n", mascara)

# 2. Le pasamos la máscara como índice al array
pares = arr2[mascara]
print("\nSolo los números pares:", pares)

# 3. Podemos sobrescribir datos usando la máscara
# Reemplazaremos todos los impares por 0
arr2[arr2 % 2 != 0] = 0
print("\nMatriz con impares apagados:\n", arr2)
```

**La función `np.where()`**

A veces no quieres el dato extraído, sino saber **dónde (en qué índices numéricos)** se cumple la condición. Para esto existe `np.where()`. Retorna las coordenadas de los `True`.

```python
# ¿Dónde están los números mayores a 10 en la matriz original?
indices_mayores_10 = np.where(arr2 > 10)
print("Índices de elementos > 10:", indices_mayores_10)
```

---
#### 🛠️ Práctica 4: Filtros Booleanos

Crea una matriz 1D (vector) que contenga todos los números del 1 al 20. Luego:
1. Utiliza una máscara booleana para encontrar y almacenar en una variable todos los números **múltiplos de 3**.
2. Sobrescribe directamente en el array original todos los valores mayores a 15 con el número `-1`. Imprime la matriz.

```python
# Escribe tu código aquí

# vector = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
vector = np.arange(1, 21)

# 1. Múltiplos de 3
multiplos_tres = vector[vector % 3 == 0]
print("Múltiplos de 3:", multiplos_tres)

# 2. Modificando in-place
vector[vector > 15] = -1
print("Vector final:", vector)
```
</details>

---
🤓 [Aprende más sobre indexación avanzada aquí.](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing)

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
