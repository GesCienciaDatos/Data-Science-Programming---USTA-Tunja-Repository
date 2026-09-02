# 06_Temas_Avanzados_Numpy_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 06. Temas Avanzados de NumPy
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/Para%20Dummies/06_Temas_Avanzados_Numpy_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. Generación de Números Aleatorios (`np.random`) 🎲

En Ciencia de Datos simulamos escenarios de negocio, inicializamos modelos de Machine Learning y dividimos datos usando números aleatorios controlados mediante una **semilla (`seed`)** para que los resultados sean reproducibles.

```python
import numpy as np

# Fijamos la semilla para que los números siempre salgan idénticos en cualquier computadora:
np.random.seed(42)

# Simular 5 lanzamientos de un dado (enteros del 1 al 6):
dados = np.random.randint(1, 7, size=5)
print("🎲 Lanzamiento de 5 dados:", dados)

# Simular 4 estaturas de personas con distribución normal (media = 1.70 m, desviación = 0.08 m):
estaturas_simuladas = np.random.normal(loc=1.70, scale=0.08, size=4)
print("📏 Estaturas simuladas:", np.round(estaturas_simuladas, 2))
```

---
## 2. La función `np.where()`: El Condicional Vectorizado 🚦

### 💡 La Analogía de la Clasificación en Línea
`np.where(condicion, valor_si_cumple, valor_si_no_cumple)` es como un inspector que dice: *"A todos los que tengan nota $\ge 3.0$ ponles 'Aprobado', a los demás ponles 'Reprobado'"* en un solo paso.

```python
notas = np.array([4.2, 2.5, 3.8, 1.9, 5.0, 3.0])

# Clasificación masiva instantánea:
estados = np.where(notas >= 3.0, "Aprobado ✅", "Reprobado ❌")

for nota, estado in zip(notas, estados):
    print(f"Nota: {nota} -> {estado}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
