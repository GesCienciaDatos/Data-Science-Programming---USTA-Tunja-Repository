# 01_Creacion_de_Arrays_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Creación de Arrays en NumPy
      </h1>
      <p style="margin: 6px 0 0 0; color: #b45309; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #92400e; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #f59e0b; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        💡 Para Dummies • Módulo 02
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/01_Creacion_de_Arrays_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Cómo crear Arrays en NumPy? 🏗️

Existen varias formas sencillas de crear arrays según lo que necesites:

| Función | 💡 Analogía Cotidiana | ¿Para qué sirve? |
|---|---|---|
| `np.array([1, 2, 3])` | Convertir tu lista escrita a mano en una barra de metal sólida. | Convierte listas o tuplas existentes en arrays de NumPy. |
| `np.zeros((3, 3))` | Una pizarra en blanco con cuadrícula lista para rellenar. | Crea una matriz llena solo de ceros `0`. |
| `np.ones((2, 4))` | Una hoja de sellos donde cada casilla vale `1`. | Crea una matriz llena solo de unos `1`. |
| `np.full((2, 3), 7)` | Un casillero donde pusiste el número `7` en todas las gavetas. | Llena la matriz con cualquier valor constante. |
| `np.arange(0, 10, 2)` | Un contador de pasos que da saltos fijos (0, 2, 4, 6, 8). | Secuencia con tamaño de paso conocido. |
| `np.linspace(0, 1, 5)` | Una regla graduada dividida en 5 marcas exactamente iguales. | Divide un intervalo en $N$ puntos equiespaciados. |
| `np.eye(4)` | Una matriz identidad (unos en la diagonal principal). | Fundamental en transformaciones de álgebra y matrices. |

```python
import numpy as np

# 1. A partir de una lista:
ventas_diarias = np.array([150, 220, 180, 310, 400])
print("Array de Ventas:", ventas_diarias)

# 2. Matriz de ceros (3 filas x 4 columnas)
tablero_ceros = np.zeros((3, 4))
print("\nMatriz de Ceros 3x4:\n", tablero_ceros)

# 3. Secuencia con np.arange (de 10 a 50 de 5 en 5):
secuencia = np.arange(10, 55, 5)
print("\nSecuencia arange:", secuencia)

# 4. Regla graduada con np.linspace (de 0 a 100 dividido en 5 partes exactas):
regla = np.linspace(0, 100, 5)
print("\nRegla linspace:", regla)
```

---
## 2. Atributos Fundamentales de un Array: `shape`, `ndim`, `dtype` 📏

Para inspeccionar la "anatomía" de cualquier array:
* **`.ndim`:** Número de dimensiones (1D = vector, 2D = tabla/matriz, 3D = cubo/volumen).
* **`.shape`:** La forma o dimensiones (filas, columnas).
* **`.size`:** Número total de elementos dentro de la caja.
* **`.dtype`:** El tipo de dato almacenado (`int32`, `float64`, etc.).

```python
matriz_ejemplo = np.array([[10, 20, 30], [40, 50, 60]])

print("Matriz:\n", matriz_ejemplo)
print(f"Dimensiones (ndim): {matriz_ejemplo.ndim} (Es una matriz 2D)")
print(f"Forma (shape):       {matriz_ejemplo.shape} (2 filas, 3 columnas)")
print(f"Total datos (size):  {matriz_ejemplo.size} elementos")
print(f"Tipo de dato (dtype):{matriz_ejemplo.dtype}")
```

---
## 🛠️ Práctica: Diseñando el Catálogo de un Negocio

**Problema:**
1. Crea un array de NumPy llamado `precios_base` con los números del `100` al `1000` con incrementos de `100`.
2. Crea una matriz de ceros de `4` filas y `2` columnas para registrar las ventas de 4 sucursales en 2 turnos (mañana y tarde).
3. Muestra en pantalla la forma (`shape`) y el total de elementos (`size`) de la matriz de sucursales.

```python
# Solución guiada:
precios_base = np.arange(100, 1100, 100)
print("1. Precios Base:", precios_base)

matriz_sucursales = np.zeros((4, 2))
print("\n2. Matriz Sucursales:\n", matriz_sucursales)

print(f"\n3. Forma: {matriz_sucursales.shape} (Filas: 4, Columnas: 2)")
print(f"   Total de casillas a registrar: {matriz_sucursales.size}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
