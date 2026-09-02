# 05_Concatenacion_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Concatenación y Apilamiento de Arreglos en NumPy 🔗
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/05_Concatenacion_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Concatenación y Apilamiento de Arrays en NumPy 🔗

Combinar múltiples conjuntos de datos, unir lotes de registros o ensamblar canales de imágenes son tareas rutinarias en pipelines de datos:

1. **`np.concatenate()`:** Unión de arrays a lo largo de un **eje existente** (`axis=0` o `axis=1`).
2. **`np.vstack()` y `np.hstack()`:** Apilamiento vertical y horizontal de conveniencia.
3. **`np.stack()`:** Unión de arrays a lo largo de un **NUEVO eje dimensional** (creación de tensores 3D a partir de matrices 2D).

<div align="center">
  <img src="images/stacking_concat.png" alt="Concatenación vs Apilamiento en NumPy" width="800" style="border-radius: 6px; margin: 15px 0;"/>
</div>

---
### 1. Concatenación en Ejes Existentes (`np.concatenate`) 🌱

Para concatenar arrays con `np.concatenate((a, b), axis=...)`, todas las dimensiones **excepto la del eje de concatenación** deben ser estrictamente iguales:

* **`axis=0` (Vertical / Por Filas):** Añade nuevas filas (requiere mismo número de columnas).
* **`axis=1` (Horizontal / Por Columnas):** Añade nuevas columnas (requiere mismo número de filas).

$$\begin{pmatrix} A_{2 \times 3} \\ B_{2 \times 3} \end{pmatrix} \xrightarrow{\text{axis=0}} C_{4 \times 3}, \qquad \begin{pmatrix} A_{2 \times 3} & B_{2 \times 2} \end{pmatrix} \xrightarrow{\text{axis=1}} C_{2 \times 5}$$

```python
# Configuración interactiva segura
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass
import numpy as np
```

```python
# --- EJEMPLO 2D ---
arr3 = np.arange(1, 7).reshape(2, 3)
arr4 = np.arange(7, 13).reshape(2, 3)

print("Matriz 1:\n", arr3)
print("Matriz 2:\n", arr4)
print("\nFormas 2D:", arr3.shape, arr4.shape)

# Concatenación en el Eje 0 (Hacia abajo / Filas)
# [2, 3] + [2, 3] -> [4, 3]
concat_axis_0 = np.concatenate([arr3, arr4], axis=0)
print("\nConcatenación axis=0 (Pegado Vertical):\n", concat_axis_0)
print("Nueva forma:", concat_axis_0.shape)

# Concatenación en el Eje 1 (Hacia la derecha / Columnas)
# [2, 3] + [2, 3] -> [2, 6]
concat_axis_1 = np.concatenate([arr3, arr4], axis=1)
print("\nConcatenación axis=1 (Pegado Horizontal):\n", concat_axis_1)
print("Nueva forma:", concat_axis_1.shape)
```

---
#### 🛠️ Práctica 1: Concatenando Bases de Datos

Imagina que tienes una base de datos tabular con la edad y el salario de 2 personas (matriz 2x2). Luego consigues los mismos datos para otras 3 personas (matriz 3x2). 
Usa `concatenate` para unirlas en una sola base de datos de 5 personas (matriz 5x2).

```python
grupo_a = np.array([[25, 1500], [30, 2200]]) # 2 personas, 2 variables
grupo_b = np.array([[22, 1200], [45, 3500], [38, 2800]]) # 3 personas, 2 variables

# Escribe tu código aquí

# base_completa = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Como queremos apilar más "filas" (personas), usamos axis=0
base_completa = np.concatenate([grupo_a, grupo_b], axis=0)
print(base_completa)
print("Forma final:", base_completa.shape)
```
</details>

---
### 2. Apilamiento Dimensional (*Stacking*) 🥞

A diferencia de `np.concatenate` (que une sobre un eje que ya existe), **`np.stack()` crea un nuevo eje dimensional**:

* **Apilar dos vectores 1D de longitud $n$:** Produce una matriz 2D de $(2, n)$ o $(n, 2)$.
* **Apilar tres matrices 2D de $(H, W)$:** Produce un tensor 3D de $(3, H, W)$ o $(H, W, 3)$ (ej. canales de color Rojo, Verde y Azul de una imagen).

```python
# --- EJEMPLO 1D a 2D ---
# Declaración explícita de vectores 1D
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stacking en el eje 0 (Crea la dimensión al principio: [2, 3])
stack_axis_0 = np.stack([arr1, arr2], axis=0)
print("Stack axis=0 (Crea filas):\n", stack_axis_0)
print("Forma:", stack_axis_0.shape)

# Stacking en el eje -1 (Último eje, crea columnas pareadas: [3, 2])
stack_axis_1 = np.stack([arr1, arr2], axis=-1)
print("\nStack axis=-1 (Crea columnas pareadas):\n", stack_axis_1)
print("Forma:", stack_axis_1.shape)
```

```python
# --- EJEMPLO 2D a 3D ---
# arr3 y arr4 son matrices 2x3. Al apilarlas, pasaremos al mundo 3D.

# [2, 3] y [2, 3] -> [2, 2, 3] 
# (Se crea una dimensión '2' al inicio, representando "2 matrices, cada una de 2x3")
stack_2d_ax0 = np.stack([arr3, arr4], axis=0)
print("Stack 3D (axis=0):\n", stack_2d_ax0)
print("Forma:", stack_2d_ax0.shape)

# [2, 3] y [2, 3] -> [2, 3, 2]
# (Se emparejan los elementos individuales uno detrás de otro)
stack_2d_ax_last = np.stack([arr3, arr4], axis=-1)
print("\nStack 3D (axis=-1):\n", stack_2d_ax_last)
print("Forma:", stack_2d_ax_last.shape)
```

---
#### 🛠️ Práctica 2: Apilando Capas de Color (Imágenes RGB)

En procesamiento de imágenes digitales, el color se representa separando los canales Rojo (R), Verde (G) y Azul (B). Tienes tres matrices 2D (5x5) que representan la intensidad de cada color de una minúscula imagen.
Utiliza `np.stack()` para apilarlas en el último eje (`axis=-1`) y crear un solo tensor 3D de forma `(5, 5, 3)` (Alto, Ancho, Canales).

```python
R = np.ones((5, 5)) * 255   # Canal Rojo
G = np.zeros((5, 5))        # Canal Verde
B = np.zeros((5, 5))        # Canal Azul

# Escribe tu código aquí

# imagen_rgb = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Apilamos en el último eje para que los 3 canales queden en la "profundidad" de la imagen
imagen_rgb = np.stack([R, G, B], axis=-1)

print("Forma del Tensor de Imagen:", imagen_rgb.shape)
# Si te fijas en el primer pixel [0,0], verás que tiene [255, 0, 0] (Rojo puro)
print("Pixel [0,0]:", imagen_rgb[0, 0]) 
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
