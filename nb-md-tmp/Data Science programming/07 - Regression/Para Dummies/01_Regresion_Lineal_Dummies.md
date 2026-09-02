# 01_Regresion_Lineal_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Regresión Lineal Explicada Paso a Paso
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/Para%20Dummies/01_Regresion_Lineal_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Cómo funciona la Regresión Lineal? 📏

### 💡 La Analogía del Perito Valuador de Viviendas:
Imagina a un valuador experto de finca raíz en Boyacá. Sabe que:
- Una casa vacía en lote base vale mínimo `\$50,000,000` (el intercepto o punto de partida).
- Por cada metro cuadrado adicional construido, el precio sube `\$2,500,000` (la pendiente o peso de la variable).

La fórmula matemática es exactamente esa:
$$\text{Precio Estimado} = 50,000,000 + (2,500,000 \times \text{Metros Cuadrados})$$

---
## 2. Las Métricas de Evaluación Clave:

| Métrica | 🗣️ ¿Qué significa en cristiano? | ¿Cómo se interpreta? |
|---|---|---|
| **$R^2$ (Coeficiente de Determinación)** | El porcentaje de la variación que nuestro modelo logra explicar con éxito. | Va de 0 a 1. Si $R^2 = 0.85$, significa que el modelo explica el **85% del precio de las casas** y solo un 15% queda sin explicar por azar. |
| **MAE (Error Absoluto Medio)** | En promedio, ¿por cuántos pesos o dólares le pifia el modelo a la realidad? | Si MAE = \$10M, en promedio nuestras predicciones se equivocan por $\pm \$10\text{M}$. |
| **RMSE (Raíz del Error Cuadrático Medio)** | Similar al MAE, pero castiga con mucha más severidad los errores gigantescos y garrafales. | Entre más bajo, mejor es el modelo. |

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Datos de casas (Metros cuadrados vs Precio en Millones COP):
metros_cuadrados = np.array([45, 60, 75, 90, 120, 150, 180]).reshape(-1, 1)
precios_millones = np.array([120, 155, 190, 240, 310, 390, 470])

# 1. Creamos y entrenamos el modelo:
modelo = LinearRegression()
modelo.fit(metros_cuadrados, precios_millones)

# 2. Hacemos predicciones:
predicciones = modelo.predict(metros_cuadrados)

print(f"🏠 Precio Base (Intercepto): ${modelo.intercept_:.2f} Millones")
print(f"📈 Valor por m² adicional (Pendiente): ${modelo.coef_[0]:.2f} Millones por m²")
print(f"🎯 Precisión del Modelo R²: {r2_score(precios_millones, predicciones):.1%}")
```

---
### Visualizando la Recta de Mejor Ajuste 🎨

```python
plt.figure(figsize=(8, 5))
plt.scatter(metros_cuadrados, precios_millones, color="#0284c7", s=80, label="Casas Reales Observadas")
plt.plot(metros_cuadrados, predicciones, color="#dc2626", linewidth=2.5, label="Recta de Predicción del Modelo")
plt.xlabel("Metros Cuadrados (m²)")
plt.ylabel("Precio (Millones COP)")
plt.title("Regresión Lineal: Predicción de Precios de Inmuebles")
plt.legend()
plt.show()
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
