# 04_Reshaping_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. Reshaping (Remodelado de Arrays)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/04_Reshaping_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es Reshaping? 🧱

### 💡 La Analogía de los Cubitos de Hielo y los Bloques de LEGO
Imagina que tienes 12 cubitos de hielo en una fila larga de $1 \times 12$.
Puedes reorganizar exactamente esos mismos 12 cubitos en:
- Un rectángulo de $3 \times 4$ (3 filas de 4 cubitos).
- Un rectángulo de $2 \times 6$ (2 filas de 6 cubitos).
- Un rectángulo de $6 \times 2$ o $4 \times 3$.

La única regla matemática inviolable es que el producto de las nuevas dimensiones debe ser igual al total de datos: $3 \times 4 = 12$.

```python
import numpy as np

# Creamos un vector plano con 12 números:
datos = np.arange(1, 13)
print("Forma original (1D):", datos.shape)
print("Datos:", datos)

# Lo remodelamos a una matriz de 3 filas x 4 columnas con .reshape():
matriz_3x4 = datos.reshape((3, 4))
print("\nMatriz Remodelada 3x4:\n", matriz_3x4)

# Remodelamos a 2 filas x 6 columnas:
matriz_2x6 = datos.reshape((2, 6))
print("\nMatriz Remodelada 2x6:\n", matriz_2x6)
```

---
### Aplanar una Matriz: `.ravel()` y `.flatten()` 🥞
Si tienes una tabla 2D y quieres convertirla de regreso en una lista plana de 1D:

```python
plano = matriz_3x4.flatten()
print("Array Aplanado de regreso a 1D:", plano)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
