# 04_Reshaping_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Remodelación y Transposición de Arreglos (Reshaping) 📐
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/04_Reshaping_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Remodelación de Arrays (Reshaping) y Gestión de Memoria 📐

En Machine Learning y Deep Learning, los datos deben adaptarse constantemente a las formas geométricas esperadas por los modelos (ej. transformar un vector 1D de características en una matriz $N \times p$, o aplanar imágenes 2D $28 \times 28$ a vectores de 784 elementos).

En este cuaderno aprenderás:
1. **`.reshape(shape)`:** Modificación de dimensiones preservando el número total de elementos.
2. **Dimensión Comodín `-1`:** Inferencia automática de dimensiones desconocidas.
3. **Aplanado de Arrays:** Diferencias críticas entre `.flatten()` (copia en RAM) y `.ravel()` (vista zero-copy).
4. **Orden de Memoria Contigua:** *Row-Major* (Orden C) vs *Column-Major* (Orden Fortran).

---
### 1. Cambiando la Forma (Reshape) 📐

El método `.reshape()` le otorga una nueva "forma" (dimensiones) a un array sin alterar los datos internos originales. 

**La Regla de Oro:** El array que deseas producir *debe tener exactamente el mismo número total de elementos* que el array original. 
Si tienes un vector unidimensional de 12 elementos, puedes convertirlo en una matriz de `3x4`, `4x3`, `2x6`, o `12x1`. ¡Pero si intentas hacer un `3x5` (15 espacios), NumPy arrojará un error catastrófico!

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
### 1.1 El Orden de Memoria en RAM: C vs Fortran 🧠

NumPy permite almacenar arrays contiguos en dos formatos de diseño de memoria:
* **Orden C (`order='C'` — *Row-major*):** Los elementos de la misma **fila** se almacenan consecutivamente en memoria (estándar en C/C++ y Python).
* **Orden Fortran (`order='F'` — *Column-major*):** Los elementos de la misma **columna** se almacenan consecutivamente (estándar en Fortran, MATLAB y R).

> 💡 **Impacto en Rendimiento:** Iterar o procesar arrays a lo largo del eje contiguo en memoria es hasta $5\times$ más rápido debido a los aciertos en la memoria caché L1/L2 de la CPU (*Cache Hits*).

---
#### 🛠️ Práctica 1: Matemática de Remodelación

Tienes un array 1D que contiene exactamente las 24 horas del día. Tu objetivo es convertirlo en un tensor 3D usando `.reshape()` que represente `(2 bloques de 12 horas, 3 filas, 4 columnas)`. Confirma matemáticamente en tu cabeza que `2 * 3 * 4 = 24`.

```python
horas = np.arange(1, 25)

# Escribe tu código aquí

# tensor_horas = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
tensor_horas = horas.reshape(2, 3, 4)
print(tensor_horas)
```
</details>

---
### 2. La Dimensión Comodín (-1) 💡

Hacer los cálculos multiplicativos en tu cabeza para el `reshape()` es fácil con 24 elementos. Pero, ¿y si tienes un array de 78,400 elementos y quieres que tenga exactamente 112 filas? ¿Cuántas columnas debería tener?

NumPy te permite pasar el número **`-1`** en una de las dimensiones para que él haga la matemática pesada por ti. El `-1` significa *"calcula automáticamente esta dimensión para que todo cuadre"*. ¡Ojo! Solo puedes usar un único comodín `-1` por remodelación.

```python
c = np.arange(12)

# Queremos 3 filas, pero nos da pereza calcular las columnas (sabemos que son 4)
c_reshape = c.reshape(3, -1)
print("Usando -1 en columnas:\n", c_reshape)

# Queremos 2 columnas, que él calcule las filas
c_reshape2 = c.reshape(-1, 2)
print("\nUsando -1 en filas:\n", c_reshape2)
```

---
#### 🛠️ Práctica 2: Usando el Comodín

Acabas de importar una lista gigante de precios de 100 productos diferentes. Quieres organizar estos precios de manera que cada fila contenga bloques de 5 productos. Usa el comodín `-1` para que NumPy calcule automáticamente cuántas filas vas a necesitar.

```python
precios = np.arange(1, 101) # 100 elementos

# Escribe tu código aquí

# matriz_precios = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
matriz_precios = precios.reshape(-1, 5)
print("Filas calculadas por NumPy:", matriz_precios.shape[0])
print(matriz_precios)
```
</details>

---
### 3. Aplanando Matrices: `flatten()` vs `ravel()` 🥞

Convertir una matriz multidimensional en un vector unidimensional es una operación común antes de pasar datos a algoritmos lineales:

| Método | Tipo de Retorno | Modificación del Original | Eficiencia en Memoria |
|---|---|:---:|---|
| **`.ravel()`** | **Vista (*View*)** siempre que sea posible | ⚠️ **Sí modifica el original** | Zero-copy (instantáneo, no usa RAM extra) |
| **`.flatten()`** | **Copia (*Copy*)** independiente | 🛡️ **No modifica el original** | Asigna un nuevo bloque de memoria RAM |

```python
# Demostrando el peligro de Ravel
matriz_madre = np.array([[1, 2], [3, 4]])

# Aplanamos la matriz
vector_ravel = matriz_madre.ravel()
print("Vector Ravel antes:", vector_ravel)

# Alguien decide cambiar el primer elemento del vector aplanado a 999
vector_ravel[0] = 999
print("Vector Ravel después:", vector_ravel)

# ¡OH NO! La matriz original ha sido corrompida
print("\nMatriz Madre original:\n", matriz_madre)
```

🤓 [Aprende mucho más sobre Copias vs Vistas de memoria RAM aquí.](https://numpy.org/doc/stable/user/quickstart.html#copies-and-views)

---
#### 🛠️ Práctica 3: Aplanado Seguro

Crea una matriz de ceros de 3x3. Aplánala de forma **segura** (para evitar catástrofes de memoria) y cambia todos los valores del vector aplanado por el número `5`. Imprime la matriz original 3x3 para comprobar que **NO** se modificó.

```python
# Escribe tu código aquí

# original_3x3 = ...
# plana_segura = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
original_3x3 = np.zeros((3, 3))

# Usamos flatten para hacer una copia aislada
plana_segura = original_3x3.flatten()
plana_segura[:] = 5 # Cambia todo el vector a 5

print("Matriz Original Intacta:\n", original_3x3)
print("\nVector Plano Modificado:", plana_segura)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
