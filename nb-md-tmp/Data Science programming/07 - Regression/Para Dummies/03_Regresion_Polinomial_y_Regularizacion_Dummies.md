# 03_Regresion_Polinomial_y_Regularizacion_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Regularización: Ridge, Lasso y ElasticNet
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/Para%20Dummies/03_Regresion_Polinomial_y_Regularizacion_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## El Duelo: Sobreajuste (*Overfitting*) vs Regularización 🥊

### 💡 La Analogía del Estudiante que Machetea el Examen:
- **Sobreajuste (Overfitting):** El estudiante memoriza las preguntas exactas del taller con comas y puntos. Si le cambias un solo número en el examen real, ¡saca 0 porque no aprendió la lógica de fondo!
- **Regularización (La Penalización):** Le cobramos una "multa matemática" al modelo por cada fórmula innecesariamente compleja o peso exagerado que intente usar, obligándolo a enfocarse solo en lo esencial.

---
## Los 3 Tipos de Regularización:

| Técnica | Tipo de Penalización | 💡 Superpoder Especial |
|---|---|---|
| **Ridge ($L_2$)** | Penaliza la suma de cuadrados ($eta^2$). | Reduce todos los coeficientes haciéndolos chiquitos, pero **nunca los apaga a cero**. |
| **Lasso ($L_1$)** | Penaliza la suma de valores absolutos ($|eta|$). | **Apaga a CERO absoluto** las variables inútiles (funciona como un selector automático de variables). |
| **ElasticNet** | Mezcla lo mejor de Ridge y Lasso. | Ideal cuando tienes muchas variables correlacionadas entre sí. |

```python
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

# Creamos un problema de regresión con 10 variables (donde solo 3 son realmente útiles):
X, y = make_regression(n_samples=50, n_features=10, n_informative=3, random_state=42)

# 1. Ridge:
ridge = Ridge(alpha=1.0).fit(X, y)

# 2. Lasso:
lasso = Lasso(alpha=1.0).fit(X, y)

df_coef = pd.DataFrame({
    "Variable": [f"Var_{i}" for i in range(10)],
    "Coef_Ridge": ridge.coef_.round(2),
    "Coef_Lasso (Apaga a 0 las inútiles)": lasso.coef_.round(2)
})

display(df_coef)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
