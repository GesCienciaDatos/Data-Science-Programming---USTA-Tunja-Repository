# 02_Consideraciones_Regresion_Multiple_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Regresión Múltiple y Multicolinealidad
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/Para%20Dummies/02_Consideraciones_Regresion_Multiple_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es la Multicolinealidad? 👥 💥

Imagina que estás en un juicio y llamas a declarar a dos testigos que son hermanos gemelos idénticos, viven juntos y vieron exactamente lo mismo.
El segundo testigo no aporta ninguna información nueva: solo repite palabra por palabra lo que dijo el primero.

En Machine Learning:
- Si incluyes en el modelo `Estatura en Metros` y `Estatura en Centímetros`, ambas variables dicen **exactamente lo mismo**.
- El modelo se vuelve inestable porque no sabe a cuál de las dos atribuirle el peso.

---
### ¿Cómo detectarla? El Factor VIF (Variance Inflation Factor):
- **VIF < 5:** Todo bien, no hay redundancia peligrosa.
- **VIF > 10:** ¡Alerta roja! Las variables son prácticamente clones; debes eliminar una de ellas.

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Ejemplo con variables de inversión publicitaria:
df_publicidad = pd.DataFrame({
    "Inversion_TV": [230, 44, 17, 151, 180],
    "Inversion_Radio": [37, 39, 45, 41, 10],
    "Inversion_Periodico": [69, 45, 69, 58, 58]
})

# Calculamos el VIF para cada variable:
vif_data = pd.DataFrame()
vif_data["Variable"] = df_publicidad.columns
vif_data["VIF"] = [variance_inflation_factor(df_publicidad.values, i) for i in range(df_publicidad.shape[1])]

print("Evaluación de Multicolinealidad (VIF):")
display(vif_data)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
