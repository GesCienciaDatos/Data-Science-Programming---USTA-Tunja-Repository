# 02_Estadistica_Descriptiva_EDA_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Estadística Descriptiva para Humanos
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/Para%20Dummies/02_Estadistica_Descriptiva_EDA_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Las 3 Preguntas de la Estadística Descriptiva 🎯

| Concepto | 🗣️ ¿Qué significa en cristiano? | Ejemplo cotidiano |
|---|---|---|
| **Media (Promedio)** | La repartición equitativa si todos pusieran su dinero en un fondo común. | Si 3 amigos ganan \\$1M, \\$2M y \\$9M, el promedio es \\$4M (aunque 2 ganen menos). |
| **Mediana** | El punto medio exacto: el 50% de las personas gana menos y el 50% gana más. | En el caso anterior, la mediana es \\$2M (mucho más representativa). |
| **Moda** | El valor más repetido o popular. | La talla de camisa más vendida en una tienda (ej. "M"). |
| **Desviación Estándar** | ¿Qué tan dispersos o regados están los datos respecto al centro? | Si la temperatura promedio es 20°C con desviación de 1°C, el clima es súper estable. Si la desviación es 15°C, ¡pasa de congelador a desierto! |
| **Percentiles / Cuartiles** | Dividir a la población en 4 grupos iguales del 25%. | Q1 (25% inferior), Q2 (Mediana / 50%), Q3 (75% superior). |

```python
import pandas as pd
import numpy as np

# Datos de salarios en una pequeña empresa (en millones de COP):
salarios = pd.Series([1.8, 2.0, 2.1, 2.3, 2.5, 2.8, 3.0, 25.0]) # Nota el salario del gerente de 25M

print(f"💰 Media (Promedio):      ${salarios.mean():.2f}M  <-- (Afectada por el gerente)")
print(f"🎯 Mediana (Punto medio): ${salarios.median():.2f}M <-- (El valor real de la mayoría)")
print(f"📏 Desviación Estándar:   ${salarios.std():.2f}M")
print(f"📊 Rango Intercuartil Q1-Q3: ${salarios.quantile(0.25):.2f}M a ${salarios.quantile(0.75):.2f}M")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
