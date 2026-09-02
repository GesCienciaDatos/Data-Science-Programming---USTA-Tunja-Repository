# 05_Seleccion_Caracteristicas_y_Mutual_Information_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 05. Selección de Características e Información Mutua
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
        💡 Para Dummies • Módulo 06
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/05_Seleccion_Caracteristicas_y_Mutual_Information_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué más variables no siempre es mejor? 🌾 vs 💨

Poner 200 variables irrelevantes en un modelo es como estudiar para un examen de medicina leyendo recetas de cocina: solo conseguirás confundir a tu cerebro.

---
## Información Mutua (Mutual Information - MI Score) 💡

La Información Mutua mide **cuánto nos dice una variable sobre lo que queremos predecir**, sin importar si la relación es una línea recta, una curva o un zigzag.
- **Puntaje MI = 0.0:** La variable no aporta absolutamente nada (puro ruido al azar).
- **Puntaje MI > 0.5:** La variable es una pista de oro macizo para predecir el resultado.

```python
import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import seaborn as sns

df_tips = sns.load_dataset("tips")

# Queremos predecir la propina ('tip'):
X = df_tips[["total_bill", "size"]]
y = df_tips["tip"]

# Calculamos las puntuaciones MI:
mi_scores = mutual_info_regression(X, y, random_state=42)
df_mi = pd.Series(mi_scores, index=X.columns, name="Puntaje_MI").sort_values(ascending=False)

print("Ranking de Utilidad de Variables para Predecir Propina:")
display(df_mi)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
