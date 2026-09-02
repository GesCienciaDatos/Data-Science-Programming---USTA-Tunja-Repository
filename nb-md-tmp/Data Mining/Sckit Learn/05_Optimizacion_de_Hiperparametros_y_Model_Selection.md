# 05_Optimizacion_de_Hiperparametros_y_Model_Selection

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Optimización de Hiperparámetros y Model Selection 🎯
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining)
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 05
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/05_Optimizacion_de_Hiperparametros_y_Model_Selection.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

```python
# Configuración del entorno interactivo
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print(f"🚀 Entorno listo con Scikit-Learn versión: {sklearn.__version__}")
```

---
## Objetivos de Aprendizaje 🎯

En este cuaderno aprenderás a calibrar y optimizar flujos de minería de datos mediante técnicas avanzadas de `sklearn.model_selection`:

* **1. Parámetros vs Hiperparámetros:** Comprensión formal de la jerarquía de optimización.
* **2. Búsqueda en Grilla (`GridSearchCV`):** Exploración exhaustiva con validación cruzada.
* **3. Búsqueda Aleatoria (`RandomizedSearchCV`):** Muestreo eficiente sobre distribuciones probabilísticas (`scipy.stats`).
* **4. Optimización en Pipelines:** Convención de prefijos con doble guion bajo (`paso__parametro`).
* **5. Diagnóstico de Sesgo y Varianza:** Curvas de validación y aprendizaje.

---
### 1. Búsqueda en Grilla y Búsqueda Aleatoria 🎲

```
GridSearchCV:        RandomizedSearchCV:
[ • ][ • ][ • ]      [   ][ • ][   ]
[ • ][ • ][ • ]  vs  [ • ][   ][   ]
[ • ][ • ][ • ]      [   ][   ][ • ]
(Producto Cartesiano) (Muestreo Probabilístico)
```

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_regression
from scipy.stats import randint

X_r, y_r = make_regression(n_samples=250, n_features=5, noise=10.0, random_state=42)

pipeline = Pipeline([
    ('poly', PolynomialFeatures()),
    ('select', SelectKBest(score_func=f_regression)),
    ('scaler', StandardScaler())
])

param_dist = {
    'poly__degree': randint(1, 4),
    'select__k': randint(1, 6)
}

rand_search = RandomizedSearchCV(pipeline, param_distributions=param_dist, n_iter=8, cv=3, random_state=42)
rand_search.fit(X_r, y_r)

print("🎯 Mejores Hiperparámetros Encontrados:", rand_search.best_params_)
print(f"🎯 Mejor Score CV: {rand_search.best_score_:.4f}")
```

---
#### 🛠️ Práctica: Optimización de Hiperparámetros

**Ejercicio 1:**
Convierte el atributo `rand_search.cv_results_` en un DataFrame de Pandas y ordénalo de mayor a menor según `mean_test_score`, mostrando los parámetros evaluados y su score promedio.

```python
# Ejercicio 1
# Escribe tu código aquí

# df_cv = pd.DataFrame(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 1
df_cv = pd.DataFrame(rand_search.cv_results_)
tabla_resumen = df_cv[['params', 'mean_test_score', 'std_test_score', 'rank_test_score']].sort_values(by='rank_test_score')

print("Ranking de Combinaciones Evaluadas:")
display(tabla_resumen)
```
</details>

**Ejercicio 2:**
Construye una grilla `param_grid` para `GridSearchCV` evaluando `poly__degree: [1, 2]` y `select__k: [2, 4]`. Ajusta y extrae el mejor estimador (`best_estimator_`).

```python
# Ejercicio 2
# Escribe tu código aquí

# grid = GridSearchCV(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 2
param_grid = {
    'poly__degree': [1, 2],
    'select__k': [2, 4]
}

grid = GridSearchCV(pipeline, param_grid=param_grid, cv=3)
grid.fit(X_r, y_r)

print("Mejor Estimador en Grilla:", grid.best_params_)
print(f"Mejor Score: {grid.best_score_:.4f}")
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué se usa la convención `paso__parametro` en pipelines?**  
   *Respuesta:* Porque el pipeline necesita enrutar unívocamente el hiperparámetro hacia la etapa correspondiente sin colisiones de nombres.
2. **¿Cuándo es preferible `RandomizedSearchCV` sobre `GridSearchCV`?**  
   *Respuesta:* Cuando el espacio de búsqueda es grande o continuo, pues evalúa más valores diversos con un presupuesto computacional fijo acotado por `n_iter`.
3. **¿Qué indica un sobreajuste en una curva de validación?**  
   *Respuesta:* Una brecha amplia donde el score de entrenamiento es cercano a 1.0 mientras que el score de validación cae bruscamente.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Minería de Datos (Data Mining)</i>
  </p>
</div>
