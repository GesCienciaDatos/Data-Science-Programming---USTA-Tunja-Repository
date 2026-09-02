# 00_Introduccion_EDA_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción al Análisis Exploratorio (EDA)
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
        💡 Para Dummies • Módulo 04
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/Para%20Dummies/00_Introduccion_EDA_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es el EDA (Análisis Exploratorio de Datos)? 🕵️‍♂️

Imagina que eres un médico y llega un paciente nuevo a tu consultorio. No puedes recetarle una cirugía mayor de inmediato sin antes tomarle la temperatura, medirle la presión arterial, escuchar sus síntomas y pedir unos análisis de sangre.

En Ciencia de Datos, el **EDA es ese chequeo médico inicial**. Antes de construir modelos de Inteligencia Artificial o Machine Learning, nos ponemos la lupa de detective para responder:
- ¿Qué historias nos cuentan los datos?
- ¿Hay anomalías, errores de captura o datos sospechosos?
- ¿Qué variables están fuertemente relacionadas entre sí?

---
### Las Tres Herramientas Principales de la Visualización en Python:
1. **Matplotlib:** El motor base. Te permite personalizar cada milímetro del gráfico (colores, ejes, títulos, flechas).
2. **Seaborn:** El diseñador de moda. Crea gráficos estadísticos hermosos y modernos con una sola línea de código.
3. **Pandas Plotting:** El atajo rápido. Perfecto para hacer un gráfico exploratorio de 2 segundos directamente desde tu DataFrame con `df.plot()`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ajustamos el estilo visual para que los gráficos luzcan modernos y limpios:
sns.set_theme(style="whitegrid", palette="muted")
print("✅ Librerías de EDA configuradas correctamente.")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
