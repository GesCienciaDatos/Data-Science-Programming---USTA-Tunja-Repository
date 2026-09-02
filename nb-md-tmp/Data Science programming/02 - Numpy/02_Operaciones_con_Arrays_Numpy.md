# 02_Operaciones_con_Arrays_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Operaciones Vectorizadas y Broadcasting en NumPy ⚡
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/02_Operaciones_con_Arrays_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Operaciones Matemáticas y Broadcasting en NumPy ⚙️

En este cuaderno exploraremos la verdadera potencia computacional de NumPy:
1. **Aritmética Vectorizada:** Operaciones elemento a elemento ejecutadas a nivel de hardware sin bucles de Python.
2. **Broadcasting (*Difusión*):** El mecanismo matemático que permite operar arrays de diferentes dimensiones.
3. **Funciones Universales (*ufuncs*):** Operaciones matemáticas avanzadas (`sin`, `exp`, `log`, `sqrt`).
4. **Agregaciones Estadísticas:** Reducción de datos a lo largo de ejes (`axis=0` y `axis=1`).
5. **Álgebra Lineal Básica:** Multiplicación de matrices (`@`), transposición y producto punto.

---
### 1. Operaciones Aritméticas Vectorizadas Elemento a Elemento 🌱

En NumPy, los operadores matemáticos estándar (`+`, `-`, `*`, `/`, `**`, `//`, `%`) se aplican automáticamente **elemento a elemento (*element-wise*)** sobre los arrays:

$$C_{ij} = A_{ij} \odot B_{ij}$$

> ⚠️ **Atención:** El operador `*` en NumPy realiza **multiplicación elemento a elemento**, NO multiplicación matricial de álgebra lineal.

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
##### 🛠️ Práctica 1: Aritmética Básica

Imagina que tienes una matriz que representa el inventario de dos productos en tres tiendas (`inventario`), y te acaba de llegar un cargamento idéntico para cada tienda que quieres sumar al total (`llegada`).
Usa NumPy para sumar ambos arrays. Luego, asume que se dañó 1 producto de todos los lotes, así que réstale el escalar `1` a tu matriz resultante.

```python
inventario = np.array([[10, 15, 20], [5, 10, 8]])
llegada = np.array([[5, 5, 5], [2, 2, 2]])

# Escribe tu código aquí

# nuevo_inventario = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
nuevo_inventario = inventario + llegada
inventario_final = nuevo_inventario - 1

print("Inventario Final:\n", inventario_final)
```
</details>

---
### 2. El Mecanismo de Broadcasting (Difusión Dimensional) 📡

**Broadcasting** describe cómo NumPy maneja arrays de diferentes formas geométricas durante las operaciones aritméticas. El array más pequeño se "difunde" o expande virtualmente a lo largo del array más grande sin duplicar datos en la memoria RAM.

#### 📐 Las Reglas Formales del Broadcasting:
Dos dimensiones son **compatibles** si:
1. Son exactamente **iguales** ($d_1 = d_2$), o
2. Una de ellas es igual a **1** ($d_1 = 1$ o $d_2 = 1$).

Si una dimensión es 1, se estira automáticamente para igualar la otra dimensión durante el cálculo.

$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}_{2 \times 3} + \begin{pmatrix} 10 & 20 & 30 \end{pmatrix}_{1 \times 3} = \begin{pmatrix} 11 & 22 & 33 \\ 14 & 25 & 36 \end{pmatrix}_{2 \times 3}$$

<div align="center">
  <img src="images/broadcasting.png" alt="NumPy Broadcasting" width="600" style="border-radius: 6px; margin: 15px 0;"/>
</div>

```python
# Un array (vector) y un escalar numérico
distancias_millas = np.array([1.0, 2.0, 5.0, 10.0])

# El número 1.6 hace 'broadcast' internamente a [1.6, 1.6, 1.6, 1.6] de forma ultrarrápida
distancias_km = distancias_millas * 1.6
print("Conversión a KM:", distancias_km)
```

⚠️ **Nota sobre la compatibilidad:** Las dimensiones de tu array deben ser compatibles. Esto sucede cuando son iguales, o cuando una de las dimensiones es `1`. Si las dimensiones son totalmente asimétricas e incompatibles (ej. multiplicar una matriz 3x3 con un vector de 2 elementos), obtendrás un `ValueError`.

---
##### 🛠️ Práctica 2: Broadcasting

Tienes un array que representa los precios de 4 artículos en Dólares (`precios_usd`). Utilizando broadcasting, multiplica todo el array por la tasa de cambio actual (ej. `4000`) para obtener `precios_cop`.

```python
precios_usd = np.array([19.99, 5.50, 100.0, 0.99])

# Escribe tu código aquí

# precios_cop = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
tasa_cambio = 4000
precios_cop = precios_usd * tasa_cambio

print("Precios en COP:", precios_cop)
```
</details>

---
### 3. Agregaciones Estadísticas y el Parámetro `axis` 📊

NumPy incluye funciones de reducción estadística altamente optimizadas (`sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`).

#### 🧭 Comprensión Intuitiva del Parámetro `axis`:
* **Sin `axis` (por defecto):** Reduce toda la matriz a un único escalar escalar global.
* **`axis=0` (Reducción a lo largo de las filas):** Aplica la operación verticalmente, calculando el resultado **para cada columna** (retorna un vector con tantas columnas como la matriz original).
* **`axis=1` (Reducción a lo largo de las columnas):** Aplica la operación horizontalmente, calculando el resultado **para cada fila** (retorna un vector con tantas filas como la matriz original).

```
         axis=1 ──► (por cada fila)
         ┌───────────────┐
         │ 10   20   30  │ ──► mean = 20.0
axis=0   │ 40   50   60  │ ──► mean = 50.0
  │      └───────────────┘
  ▼          │    │    │
 mean:      25.0 35.0 45.0
```

```python
a = np.array([
    [0.45053314, 0.17296777, 0.34376245, 0.5510652],
    [0.54627315, 0.05093587, 0.40067661, 0.55645993],
    [0.12697628, 0.82485143, 0.26590556, 0.56917101]
])

print("Suma total de toda la matriz:", a.sum())
print("Valor mínimo en toda la matriz:", a.min())
print("Promedio global de toda la matriz:", a.mean())
```

**El parámetro Mágico: `axis`**

Rara vez querrás el promedio de toda tu hoja de cálculo. Generalmente querrás "el promedio de cada columna" (ej. temperatura media diaria) o "la suma de cada fila" (ej. notas totales por estudiante).

El parámetro `axis` (eje) controla cuál dimensión será "colapsada" matemáticamente:
*   `axis=0`: Recorre la matriz verticalmente hacia abajo. Colapsa las filas, entregando un resultado **por columna**.
*   `axis=1`: Recorre la matriz horizontalmente. Colapsa las columnas, entregando un resultado **por fila**.

```python
# Retorna el valor mínimo contenido en CADA COLUMNA
# Al haber 4 columnas, obtenemos 4 resultados.
print("Mínimos por Columna (axis=0):", a.min(axis=0))

# Retorna la suma contenida en CADA FILA
# Al haber 3 filas, obtenemos 3 resultados.
print("Suma por Fila (axis=1):", a.sum(axis=1))
```

---
##### 🛠️ Práctica 3: Agregando por Ejes

Imagina que la siguiente matriz de 3x3 representa las notas de 3 estudiantes (las filas) en 3 asignaturas distintas (las columnas).

```python
notas = np.array([
    [3.5, 4.0, 4.2], # Estudiante 1
    [2.8, 3.1, 4.0], # Estudiante 2
    [4.5, 4.6, 4.8]  # Estudiante 3
])
```

Calcula e imprime:
1. La **nota máxima** obtenida en cada asignatura (`axis=0`).
2. El **promedio** de notas de cada estudiante (`axis=1`).

```python
notas = np.array([
    [3.5, 4.0, 4.2],
    [2.8, 3.1, 4.0],
    [4.5, 4.6, 4.8] 
])

# Escribe tu código aquí

# maximas_asignaturas = ...
# promedios_estudiantes = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
maximas_asignaturas = notas.max(axis=0)
promedios_estudiantes = notas.mean(axis=1)

print("Nota máxima por materia:", maximas_asignaturas)
print("Promedio por estudiante:", promedios_estudiantes)
```
</details>

---
### 4. Álgebra Lineal: Multiplicación Matricial (`@` / `np.dot`) 🧮

Para realizar la **multiplicación matricial formal** de álgebra lineal (donde el número de columnas de $A$ debe coincidir con el número de filas de $B$), utilizamos el operador **`@`** (introducido en Python 3.5+) o `np.dot()`:

$$C_{m \times p} = A_{m \times n} \times B_{n \times p}, \quad C_{ij} = \sum_{k=1}^n A_{ik} B_{kj}$$

* **Transposición de Matrices:** La propiedad `.T` intercambia filas por columnas ($A^T_{ij} = A_{ji}$).

```python
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print("Producto elemento a elemento (A * B):")
print(A * B)

print("\nProducto de Matrices de Álgebra Lineal (A @ B):")
print(A @ B)

print("\nTransposición (A.T):")
print("Matriz A original:\n", A)
print("Matriz A transpuesta:\n", A.T)
```

---
##### 🛠️ Práctica 4: Álgebra Matricial

Dadas las matrices `X` e `Y`, transpone la matriz `X` y luego realiza el producto matricial entre tu nueva matriz transpuesta de X y la matriz Y. (Asegúrate de usar `@` o `.dot()`).

```python
X = np.array([[1, 2], [3, 4], [5, 6]]) # Matriz 3x2
Y = np.array([[1, 0, 1], [0, 1, 0]]) # Matriz 2x3

# Escribe tu código aquí

# X_transpuesta = ...
# producto = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
X_transpuesta = X.T

# X_transpuesta ahora es 2x3. Multiplicada por Y que es 2x3... ¡Espera! 
# Las matemáticas dictan que no podemos multiplicar 2x3 con 2x3.
# Multipliquemos la original (3x2) por Y (2x3):
producto = X @ Y 
print("Producto Matricial (3x3):\n", producto)

# Si queríamos multiplicar la transpuesta de X (2x3), 
# necesitaríamos que Y también estuviera transpuesta (3x2)
print("\nProducto de ambas transpuestas (2x2):\n", X.T @ Y.T)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
