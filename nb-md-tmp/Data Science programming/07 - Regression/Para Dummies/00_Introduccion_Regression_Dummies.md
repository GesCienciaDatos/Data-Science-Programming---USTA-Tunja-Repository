# 00_Introduccion_Regression_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción a Modelos de Regresión
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
        💡 Para Dummies • Módulo 07
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/Para%20Dummies/00_Introduccion_Regression_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es la Regresión y en qué se diferencia de la Clasificación? 🎯

En Machine Learning Supervisado resolvemos dos grandes tipos de preguntas:

| Tipo de Problema | 💡 Pregunta que responde | Tipo de Respuesta | Ejemplos |
|---|---|---|---|
| **Clasificación** | ¿A qué categoría pertenece? | Etiqueta discreta (Sí/No, Spam/No Spam, Perro/Gato). | ¿El cliente cancelará la tarjeta? ¿La transacción es fraude? |
| **Regresión** | **¿Cuánto vale o qué cantidad será?** | **Número continuo infinito.** | **¿Cuánto costará esta casa? ¿Cuántas ventas tendremos el próximo mes? ¿Qué temperatura hará mañana?** |

---
### El Camino de Aprendizaje del Módulo 07:
1. **Regresión Lineal Simple y Múltiple:** Trazar la mejor recta predictora.
2. **Evaluación de Modelos:** Entender $R^2$ (qué porcentaje explicamos) y RMSE (el error en dinero o unidades reales).
3. **Regularización (Ridge y Lasso):** Ponerle un freno al modelo para que no invente historias falsas.
4. **Validación Cruzada (Cross-Validation) y k-NN:** Poner a prueba el modelo en simulacros reales.

```python
import sklearn
import numpy as np
import pandas as pd

print("✅ Entorno de Modelado y Regresión listo.")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
