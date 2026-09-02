# 00_Introduccion_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción a NumPy
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/00_Introduccion_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué las listas normales no son suficientes? 🐌 vs 🚀

Hasta ahora aprendiste a usar listas en Python (`[10, 20, 30]`). Las listas son maravillosas para guardar cosas variadas, pero cuando trabajas en Ciencia de Datos con **100,000 transacciones bancarias, millones de píxeles de imágenes o registros médicos**, las listas normales se vuelven extremadamente lentas.

### 💡 La Analogía del Supermercado:
- **La Lista Tradicional de Python:** Es como ir al supermercado con una canasta desordenada donde metes una manzana, un libro de historia, un zapato y una botella de leche. Python tiene que revisar qué es cada objeto uno por uno para no equivocarse.
- **El Array de NumPy (`ndarray`):** Es una **caja estandarizada de fábrica** donde todos los compartimentos contienen exactamente el mismo tipo de objeto (por ejemplo, solo números decimales). Como todos son iguales y están pegaditos en la memoria de la computadora, ¡puedes procesar toda la caja de un solo golpe a la velocidad de la luz!

---
### ¿Qué significa NumPy?
NumPy significa **Numerical Python**. Fue escrita en lenguaje C/Fortran de ultra alto rendimiento y es la base sobre la que se construyen **Pandas, Matplotlib, Scikit-Learn y la Inteligencia Artificial**.

```python
import numpy as np
import time

print(f"✅ NumPy importado con éxito. Versión: {np.__version__}")
```

---
## Demostración de Velocidad: Lista vs NumPy ⚡

Vamos a comparar cuánto tarda Python en elevar al cuadrado 1,000,000 de números usando una lista tradicional vs un array de NumPy:

```python
# 1. Con lista tradicional de Python:
lista_millon = list(range(1_000_000))
inicio_lista = time.time()
resultado_lista = [x ** 2 for x in lista_millon]
tiempo_lista = time.time() - inicio_lista

# 2. Con NumPy Array:
array_millon = np.arange(1_000_000)
inicio_numpy = time.time()
resultado_numpy = array_millon ** 2  # ¡Operación directa y limpia!
tiempo_numpy = time.time() - inicio_numpy

print(f"⏱️ Tiempo con Lista tradicional: {tiempo_lista:.5f} segundos")
print(f"🚀 Tiempo con NumPy Array:      {tiempo_numpy:.5f} segundos")
print(f"👉 ¡NumPy fue aproximadamente {int(tiempo_lista / tiempo_numpy)} veces más rápido!")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
