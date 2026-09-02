# 01_Creacion_de_Arrays_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Creación y Atributos de Arreglos en NumPy 🧱
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/01_Creacion_de_Arrays_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Creación de Arrays en NumPy 🏗️

El bloque de construcción fundamental de NumPy es el **`ndarray`** (*N-dimensional array*). Un array es una cuadrícula de valores, **todos del mismo tipo de datos (*homogéneos*)**, indexados por una tupla de enteros no negativos.

### Dimensiones en NumPy:
* **1D Array (Vector):** Colección lineal de elementos (forma `(n,)`).
* **2D Array (Matriz):** Tabla bidimensional organizada en filas y columnas (forma `(m, n)`).
* **3D+ Array (Tensor):** Arreglos multidimensionales (forma `(k, m, n)`), esenciales para representar imágenes a color, lotes de series temporales o tensores de Deep Learning.

> 💡 **Regla Fundamental:** A diferencia de las listas de Python, un `ndarray` debe tener un tipo de dato (`dtype`) homogéneo y una forma (`shape`) geométrica bien definida.

---
### 1. Creación Básica desde Listas y Atributos Fundamentales 🌱

La función `np.array()` convierte listas o tuplas de Python en un arreglo de NumPy.

#### Atributos Esenciales de un `ndarray`:
* **`.ndim`:** Número de dimensiones o ejes (*rank* del array).
* **`.shape`:** Tupla de enteros que indica el tamaño del array en cada dimensión `(filas, columnas, ...)`.
* **`.size`:** Número total de elementos contenidos en el array ($\prod \text{shape}$).
* **`.dtype`:** Tipo de dato de los elementos (`int32`, `float64`, `bool_`, etc.).
* **`.itemsize`:** Tamaño en bytes de cada elemento individual en memoria.

---
#### 1.1 Desde listas de Python

La forma más básica de crear un array es tomar una lista estándar de Python e inyectarla en NumPy a través de la función `np.array()`.

**¿Por qué convertir una lista a un array?**
* **Las listas de Python** son flexibles: pueden contener enteros, strings y booleanos al mismo tiempo, pero esta flexibilidad las hace muy lentas para calcular matemáticas masivas.
* **Los arrays de NumPy** son rígidos: **todos** los elementos en un array deben ser estrictamente del mismo tipo numérico. Al quitar esa flexibilidad, NumPy puede agrupar la memoria y realizar operaciones matemáticas miles de veces más rápido en código C precompilado.

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
##### 🛠️ Práctica 1.1: Arrays desde listas

Crea una lista anidada en Python que represente una cuadrícula de 2 filas y 2 columnas con los números del 1 al 4. Luego conviértela a un array de NumPy e imprímela.

```python
# Escribe tu código aquí

# lista_2x2 = ...
# array_practica_1 = ...
```

---
### 2. Métodos Constructores de Inicialización Rápida 🛠️

En Ciencia de Datos, a menudo necesitamos inicializar matrices con valores constantes (ceros, unos o valores específicos) antes de utilizarlas en algoritmos de optimización o redes neuronales:

| Función | Descripción | Ejemplo | Forma Resultante |
|---|---|---|:---:|
| `np.zeros(shape)` | Crea un array relleno con ceros (`0.0`). | `np.zeros((3, 4))` | Matriz $3 \times 4$ de ceros |
| `np.ones(shape)` | Crea un array relleno con unos (`1.0`). | `np.ones((2, 3))` | Matriz $2 \times 3$ de unos |
| `np.full(shape, val)` | Crea un array relleno con un valor constante `val`. | `np.full((3, 3), 7.5)` | Matriz $3 \times 3$ de 7.5 |
| `np.empty(shape)` | Asigna memoria sin inicializar valores (ultrarrápido). | `np.empty((2, 2))` | Matriz $2 \times 2$ con valores residuales |

---
#### 1.2 Funciones integradas (Zeros, Ones, Empty)

A menudo en ciencia de datos, necesitas inicializar una matriz de cierto tamaño antes de saber exactamente qué valores irán adentro (por ejemplo, para guardar los resultados de un bucle). Escribir listas anidadas a mano sería imposible para matrices enormes.

Para ello usamos tres funciones clave:

1. **`np.zeros(shape)`**: Crea un array lleno de ceros (`0`). 
   * **¿Para qué sirve?** Funciona como un "lienzo en blanco" (placeholder). Inicializar con ceros garantiza que no haya valores residuales de memoria y es la opción más segura.
2. **`np.ones(shape)`**: Crea un array lleno de unos (`1`).
   * **¿Para qué sirve?** Es útil cuando la inicialización requiere un valor neutral para multiplicaciones matriciales o para aplicar operaciones algebraicas base.
3. **`np.empty(shape)`**: Crea un array asignando el espacio en memoria **sin limpiarlo**. 
   * **¿Para qué sirve?** Es la forma absolutamente más **rápida** de crear un array grande porque no gasta tiempo de CPU escribiendo ceros en la RAM. Sin embargo, el array se creará con "basura" (los últimos números que tu computadora tuvo en ese sector de RAM). ¡Solo úsalo si estás 100% seguro de que vas a sobrescribir **cada uno** de sus elementos inmediatamente después!

```python
print("Zeros (Vector 1D):")
print(np.zeros(3))

print("\nOnes (Matriz 2x2):")
print(np.ones((2, 2))) # Nota que pasamos una tupla (2, 2) para el 'shape'

print("\nEmpty (Cuidado con la 'basura' de memoria):")
print(np.empty(4))
```

---
##### 🛠️ Práctica 1.2: Inicialización rápida

Utiliza funciones integradas para:
1. Crear una matriz de 4 filas y 3 columnas llena de ceros.
2. Crear un vector de 5 elementos lleno de unos.

```python
# Escribe tu código aquí
```

---
### 3. Secuencias Numéricas y Rangos (`arange` vs `linspace`) 🧠

NumPy ofrece dos funciones fundamentales para generar secuencias numéricas continuas o discretas:

1. **`np.arange(start, stop, step)`:** Genera valores espaciados por un **paso (*step*)** definido en el intervalo $[start, stop)$.
2. **`np.linspace(start, stop, num)`:** Genera un número exacto **`num`** de valores linealmente espaciados en el intervalo cerrado $[start, stop]$.

$$\text{Paso en linspace} = \frac{stop - start}{num - 1}$$

> 📌 **¿Cuándo usar cuál?**
> * Usa **`np.arange`** cuando conozcas con precisión el *tamaño del paso* (ej. dar saltos de \$0.5$).
> * Usa **`np.linspace`** cuando conozcas con precisión el *número de puntos deseados* (ej. generar \$100$ puntos para graficar una curva continua con Matplotlib).

---
#### 1.3 Funciones de Rango y Secuencia (Arange, Linspace)

Cuando trabajas con gráficas, series de tiempo o ejes continuos, necesitarás generar rangos matemáticos exactos.

1. **`np.arange(inicio, fin, paso)`**:
   * Funciona casi idéntico al `range()` nativo de Python, pero retorna un array de NumPy y admite saltos (pasos) con decimales.
   * El límite `fin` siempre es **excluyente** (no se incluye).
   * **Uso ideal:** Cuando sabes exactamente de a cuánto quieres que salten los números (ej. saltar de a `0.5`).

2. **`np.linspace(inicio, fin, cantidad_elementos)`**:
   * En lugar de especificar de a cuánto saltar, tú especificas cuántos números totales quieres tener al final. NumPy hace la matemática y calcula el paso exacto para que estén espaciados de manera perfectamente uniforme.
   * El límite `fin` aquí **SÍ** se incluye por defecto.
   * **Uso ideal:** Especialmente útil en Machine Learning y gráficas cartesianas (matplotlib) para crear los ejes de una función.

```python
print("Uso de arange (Paso conocido):")
print("De 0 a 9 (excluye 10):", np.arange(0, 10))
print("De 2 a 9 (saltando de a 2):", np.arange(2, 9, 2))

print("\nUso de linspace (Cantidad conocida):")
print("5 valores entre 0 y 10 (incluye el 10):", np.linspace(0, 10, num=5))
```

---
##### 🛠️ Práctica 1.3: Secuencias Numéricas

1. Utiliza `arange` para generar todos los números pares del 10 al 20 (incluyendo el 20). *(Pista: el límite superior debe ser 21 para que lo incluya).*
2. Utiliza `linspace` para generar exactamente 100 números espaciados entre el 0 y el 1.

```python
# Escribe tu código aquí
```

---
### 4. Matrices Especiales y Tipos de Datos Numéricos (`dtype`) 💎

#### Matrices Especiales:
* **Matriz Identidad (`np.eye(N)` / `np.identity(N)`):** Matriz cuadrada con unos en la diagonal principal y ceros en el resto ($I_N$).
* **Matriz Diagonal (`np.diag(v)`):** Construye una matriz diagonal a partir de un vector $v$ o extrae la diagonal de una matriz dada.

#### Tipos de Datos (`dtype`) y Consumo de Memoria:
NumPy soporta tipos numéricos optimizados:
* **Enteros:** `np.int8` (1 byte), `np.int16` (2 bytes), `np.int32` (4 bytes), `np.int64` (8 bytes).
* **Flotantes:** `np.float16` (media precisión), `np.float32` (precisión simple, estándar en Deep Learning/GPU), `np.float64` (doble precisión, estándar en estadística y Scikit-Learn).

---
#### 1.4 Matriz Identidad (Eye)

En el álgebra lineal computacional, la matriz identidad es una matriz cuadrada especial que tiene unos (`1`) en su diagonal principal y ceros (`0`) en el resto de posiciones.

* **¿Para qué sirve?** La matriz identidad es el equivalente matricial del número `1`. Cualquier matriz multiplicada por su matriz identidad resulta en sí misma. Es vital para resolver sistemas de ecuaciones lineales, calcular matrices inversas, realizar descomposiciones (como PCA) y entrenar modelos como la regresión lineal.
* Usamos la función **`np.eye(n)`** para crearla, donde `n` es el número de filas y columnas.

```python
print("Matriz Identidad de 3x3:")
print(np.eye(3))
```

---
##### 🛠️ Práctica 1.4: Identidad

Crea una matriz identidad de tamaño 5x5.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
identidad_5 = np.eye(5)
print(identidad_5)
```
</details>

---
### 2. Tipos de Datos (dtype) 🛠️

A diferencia de Python, que maneja los números genéricamente detrás de escena, NumPy es de bajo nivel (se acerca al lenguaje C). Por ende, requiere saber exactamente cuánta memoria física en RAM debe reservar para cada número.

Por defecto, si escribes `np.ones(5)`, NumPy asume que son puntos flotantes muy precisos (`float64`), lo que consume mucha memoria. Si sabes que solo manejarás números enteros, puedes forzar el tipo usando el atributo **`dtype`**.

**Tipos comunes:**
* `np.float64`: Decimales por defecto (alta precisión, alto consumo de memoria).
* `np.int64` o `np.int32`: Números enteros genéricos.
* `np.int8`: Enteros muy pequeños (del -128 al 127). ¡Excelente para ahorrar memoria al procesar imágenes (donde los píxeles van del 0 al 255)!

```python
# Forzamos explícitamente a que sean enteros
array_enteros = np.ones(3, dtype=np.int32)
print("Array Entero:", array_enteros)
print("Tipo del array:", array_enteros.dtype)
```

---
##### 🛠️ Práctica 2: Casteo de tipos

Crea una matriz de ceros de 2x2. Obliga a que su tipo de dato sea **entero**. Imprime la matriz y su tipo de dato para verificar.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
ceros_enteros = np.zeros((2, 2), dtype=np.int32)
print(ceros_enteros)
print("Tipo:", ceros_enteros.dtype)
```
</details>

---
### 3. Atributos de un array

Un array suele ser un contenedor de tamaño fijo de elementos del mismo tipo y tamaño. **El número de dimensiones y elementos** en un array está definido por su **forma** (`shape`). La forma de un array es **una tupla de enteros no negativos que especifican el tamaño de cada dimensión.**

**En NumPy, las dimensiones se denominan ejes.** Esto significa que si tienes un array bidimensional (2D) con este aspecto:

```python
[[0., 0., 0.],
 [1., 1., 1.]]
```

Tu array tiene 2 ejes. El primer eje tiene una longitud de 2 y el segundo eje tiene una longitud de 3.

<img src="images/numpy_axes.png" width="600"/>

Los atributos más importantes de un objeto `ndarray` son:

* **ndarray.ndim:** el **número de ejes (dimensiones)** del array.
* **ndarray.shape:** las dimensiones del array. Esta es una tupla de enteros que indica el **tamaño del array en cada dimensión**. Para una matriz con n filas y m columnas, la forma será (n,m). Por lo tanto, la longitud de la tupla shape es el número de ejes, ndim.
* **ndarray.size:** el **número total de elementos del array**. Esto es igual al producto de los elementos de shape.
* **ndarray.dtype:** un objeto que describe el **tipo de los elementos en el array**. Se pueden crear o especificar `dtype`s utilizando los tipos estándar de Python. Además, NumPy proporciona tipos propios. numpy.int32, numpy.int16 y numpy.float64 son algunos ejemplos.
* **ndarray.itemsize:** el **tamaño en bytes de cada elemento del array**. Por ejemplo, un array de elementos de tipo float64 tiene un itemsize de 8 (=64/8), mientras que uno de tipo complex32 tiene un itemsize de 4 (=32/8). Es equivalente a ndarray.dtype.itemsize.
* **ndarray.data:** el **búfer que contiene los elementos reales del array**. Normalmente, no necesitaremos usar este atributo porque accederemos a los elementos de un array utilizando las funciones de indexación.

Debemos proporcionar listas que sean coherentes con las dimensiones y tipos de los ejes. Si no proporcionamos formas (o tipos) coherentes, NumPy optará por crear arrays de tipo `object`.

```python
# NumPy convertirá las listas solo si son coherentes con las dimensiones de los ejes
# Para tener un array definido correctamente DEBEMOS tener elementos que tengan el mismo
# número de subelementos en cada eje
arr_obj = np.array([[0,1,2], [3,4,5], [6,7,8]])
arr_obj

# ¡NumPy convierte automáticamente a un tipo de dato común, si es posible!
arr_obj = np.array([[0,1,2], [3,4,"5"], [6,7,8]])
arr_obj

# De lo contrario, recurre al tipo 'object'
arr_obj = np.array([[0,1,2], [3,4,print], [6,7,8]])
arr_obj
```

---
##### 🛠️ Práctica 3: Inspeccionando arrays

A continuación crearemos un Tensor 3D simulado con unos (`np.ones`). Un tensor 3D tiene tres valores en su shape: (profundidad/hojas, filas, columnas).

Instrucciones: Crea un array de unos con la forma `(2, 3, 4)`. Imprime directamente su `shape` y su `size` total para comprobar la construcción matemática (el tamaño debería dar 24).

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
tensor_3d = np.ones((2, 3, 4))
print("Shape del tensor:", tensor_3d.shape)
print("Size total (elementos):", tensor_3d.size)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
