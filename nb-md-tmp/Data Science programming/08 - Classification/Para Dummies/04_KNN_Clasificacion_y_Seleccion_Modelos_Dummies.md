# 04_KNN_Clasificacion_y_Seleccion_Modelos_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Algoritmo k-NN [Edición Dummies] 🎯
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
        💡 Para Dummies • Módulo 08
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/Para%20Dummies/04_KNN_Clasificacion_y_Seleccion_Modelos_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de "Dime con quién andas y te diré quién eres" 👥

Imagina que llegas a un barrio nuevo:
* Para saber si un restaurante es bueno, le preguntas a tus **3 vecinos más cercanos ($k=3$)**.
* Si 2 de los 3 vecinos dicen que es excelente, tú asumes que es excelente (votación mayoritaria).

Eso es exactamente **$k$-NN ($k$-Nearest Neighbors)**:
Para clasificar un caso nuevo, busca los $k$ ejemplos más parecidos en la base de datos y vota por la mayoría.

```python
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

url = "https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/08%20-%20Classification/data/heart_disease.csv"
df = pd.read_csv(url)

X = df[['age', 'trestbps', 'thalach']]
y = df['target']

# Pipeline que primero mide con la misma regla justa (StandardScaler) y luego consulta a los 5 vecinos
modelo_vecinos = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
modelo_vecinos.fit(X, y)

paciente_nuevo = [[52, 135, 140]]
opinion = "🚨 Riesgo Detectado" if modelo_vecinos.predict(paciente_nuevo)[0] == 1 else "✅ Saludable"
print(f"El veredicto de los 5 vecinos más parecidos es: {opinion}")
```

---
##### 🎯 Reto Práctico para Dummies: ¿Qué pasa si cambiamos la cantidad de vecinos?

**Situación:** Vamos a probar consultando a **1 vecino ($k=1$)** frente a **15 vecinos ($k=15$)** para el paciente nuevo:
* Paciente: Edad = 60, Presión = 150, Frecuencia = 120

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 4 - Comparando 1 vs 15 vecinos
# =========================================================================

# 1. Modelo con 1 vecino
# mod_k1 = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1))
# mod_k1.fit(X, y)

# 2. Modelo con 15 vecinos
# mod_k15 = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=15))
# mod_k15.fit(X, y)

# 3. Predicciones
# pac = [[60, 150, 120]]
# pred_k1 = mod_k1.predict(pac)[0]
# pred_k15 = mod_k15.predict(pac)[0]
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
pac = [[60, 150, 120]]

mod_k1 = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1))
mod_k1.fit(X, y)

mod_k15 = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=15))
mod_k15.fit(X, y)

print(f"👤 Opinión de 1 solo vecino (k=1):   {'🚨 Riesgo' if mod_k1.predict(pac)[0]==1 else '✅ Sano'}")
print(f"👥 Opinión de 15 vecinos (k=15):     {'🚨 Riesgo' if mod_k15.predict(pac)[0]==1 else '✅ Sano'}")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
