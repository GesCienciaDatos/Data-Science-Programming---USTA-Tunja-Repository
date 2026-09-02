# 00_Introduccion_Data_Preparation_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción a la Preparación de Datos
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
        💡 Para Dummies • Módulo 05
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/05%20-%20Data%20Preparation/Para%20Dummies/00_Introduccion_Data_Preparation_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Regla de Oro: "Basura Entra, Basura Sale" (GIGO) 🗑️ ➡️ 🗑️

En Ciencia de Datos existe un dicho universal:
> *"Si alimentas a un modelo de Machine Learning con datos sucios, llenos de errores y desbalanceados, el modelo aprenderá conclusiones completamente falsas y peligrosas"*.

### 💡 La Analogía del Restaurante 5 Estrellas:
Un chef de alta cocina no tira las verduras con tierra, las carnes sin descongelar y las cáscaras de huevo directamente a la sartén.
Dedica el 80% de su tiempo a la **preparación previa (*mise en place*)**: lavar, pelar, cortar en trozos exactos, medir y ordenar todos los ingredientes.

En este módulo aprenderás las 3 habilidades maestras de la limpieza:
1. **Tratar valores faltantes (casillas vacías).**
2. **Escalar variables numéricas para que ninguna opaque a las demás.**
3. **Parsear fechas y corregir errores tipográficos con coincidencia difusa (*Fuzzy Matching*).**

```python
import pandas as pd
import numpy as np
import sklearn

print("✅ Entorno de Limpieza y Preparación listo.")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
