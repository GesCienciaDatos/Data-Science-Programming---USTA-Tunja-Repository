# 02_Operaciones_con_Arrays_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Operaciones Matemáticas y Broadcasting
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/02_Operaciones_con_Arrays_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. Operaciones Vectorizadas (Element-wise) ⚡

En Python clásico, para sumarle \\$10 a todos los precios de una lista necesitabas hacer un bucle `for`.
En NumPy, simplemente escribes: `precios + 10` y NumPy se encarga de aplicarlo a cada elemento de forma automática e instantánea.

### 💡 La Analogía del Sello Automático:
Imagina que tienes 1,000 facturas sobre la mesa. En lugar de sellar una por una, tienes una máquina que estampa el sello con la fecha en todas las facturas al mismo milisegundo.

```python
import numpy as np

precios_usd = np.array([25.0, 50.0, 120.0, 15.5])
tasa_cambio_cop = 4100

# Multiplicación directa de todo el array por un número:
precios_cop = precios_usd * tasa_cambio_cop
print("Precios en USD:", precios_usd)
print("Precios en COP:", precios_cop)

# Aplicar un descuento del 10% a todos:
precios_con_descuento = precios_cop * 0.90
print("Precios con 10% de Descuento:", precios_con_descuento)
```

---
## 2. Estadísticas Agregadas: `mean()`, `sum()`, `min()`, `max()`, `std()` 📊

NumPy calcula resúmenes estadísticos a la velocidad del rayo. Además, con el parámetro `axis` puedes elegir si calcular por filas o por columnas:
- **`axis=0`:** Aplica la operación a lo largo de las **columnas** (baja verticalmente).
- **`axis=1`:** Aplica la operación a lo largo de las **filas** (recorre horizontalmente).

```python
# Matriz de calificaciones: 3 estudiantes (filas) en 4 materias (columnas)
calificaciones = np.array([
    [4.5, 3.8, 4.0, 4.9],  # Estudiante 1
    [3.0, 3.5, 2.8, 3.2],  # Estudiante 2
    [4.8, 5.0, 4.7, 4.9]   # Estudiante 3
])

print("Promedio general de toda la clase:", np.mean(calificaciones))
print("Promedio de CADA estudiante (axis=1 - filas):", np.mean(calificaciones, axis=1))
print("Promedio de CADA materia (axis=0 - columnas):", np.mean(calificaciones, axis=0))
print("Nota más alta registrada:", np.max(calificaciones))
print("Nota más baja registrada:", np.min(calificaciones))
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
