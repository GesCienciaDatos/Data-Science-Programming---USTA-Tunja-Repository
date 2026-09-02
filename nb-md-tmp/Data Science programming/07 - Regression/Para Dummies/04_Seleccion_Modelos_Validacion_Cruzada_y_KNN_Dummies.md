# 04_Seleccion_Modelos_Validacion_Cruzada_y_KNN_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. Validación Cruzada (Cross-Validation) y k-NN
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/Para%20Dummies/04_Seleccion_Modelos_Validacion_Cruzada_y_KNN_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. Validación Cruzada K-Fold (El Simulacro de Examen) 🔄

### 💡 La Analogía de las 5 Pruebas ICFES:
En lugar de calificar tu conocimiento con una sola prueba de 10 minutos (donde pudiste tener mala suerte), dividimos las preguntas en 5 secciones.
Entrenas con 4 secciones y te evalúas con la quinta. Luego rotas y repites el proceso 5 veces. El promedio de las 5 notas es tu **verdadero nivel de dominio**.

---
## 2. El Regresor k-NN (k Vecinos Más Cercanos) 🏘️

### 💡 La Analogía del Vecindario:
*"Dime cuánto valen las 5 casas más parecidas y cercanas a la tuya, y te diré exactamente cuánto vale tu casa"*.
k-NN no busca una fórmula matemática rígida: simplemente busca a los $k$ vecinos más similares en los datos históricos y promedia sus valores.

```python
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

# Generamos datos de prueba:
np.random.seed(42)
X = np.random.rand(100, 3)
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100) * 0.1

# Evaluamos con 5-Fold Cross Validation:
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Modelo 1: Regresión Lineal
scores_lr = cross_val_score(LinearRegression(), X, y, cv=kfold, scoring="r2")

# Modelo 2: k-NN Regressor (5 vecinos)
scores_knn = cross_val_score(KNeighborsRegressor(n_neighbors=5), X, y, cv=kfold, scoring="r2")

print(f"📊 Regresión Lineal R² Promedio (5 Folds): {scores_lr.mean():.1%}")
print(f"🏘️ k-NN Regressor   R² Promedio (5 Folds): {scores_knn.mean():.1%}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
