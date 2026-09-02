# 03_Indexacion_y_Slicing_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Indexación, Slicing y Filtros Booleanos
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/03_Indexacion_y_Slicing_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Cómo elegir elementos en Matrices 2D? 🎯

En NumPy usamos la notación: **`array[fila, columna]`** (separados por coma).

### 💡 La Analogía del Juego de Batalla Naval:
Para disparar en el tablero dices: *"Fila 2, Columna 3"*. En NumPy es idéntico: `matriz[2, 3]`.

```python
import numpy as np

# Matriz 3x3:
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matriz Completa:\n", matriz)
print("\nElemento en fila 0, columna 0:", matriz[0, 0])
print("Elemento en fila 1, columna 2:", matriz[1, 2])
print("Toda la fila 0 (matriz[0, :]):", matriz[0, :])
print("Toda la columna 1 (matriz[:, 1]):", matriz[:, 1])
```

---
## 2. Filtros con Máscaras Booleanas (El superpoder de NumPy) 🦸‍♂️

¿Quieres encontrar todos los números mayores a 50 sin hacer ningún bucle?
Simplemente preguntas `matriz > 50` y usas esa condición como filtro.

```python
edades = np.array([14, 25, 17, 30, 42, 16, 19, 55])

# Creamos la máscara booleana:
es_mayor_de_edad = edades >= 18
print("Máscara Booleana (True/False):", es_mayor_de_edad)

# Filtramos pasando la máscara al array:
solo_mayores = edades[es_mayor_de_edad]
print("Solo mayores de edad filtrados:", solo_mayores)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
