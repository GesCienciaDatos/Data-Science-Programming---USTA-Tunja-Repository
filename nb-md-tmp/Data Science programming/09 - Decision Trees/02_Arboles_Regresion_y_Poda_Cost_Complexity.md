# 02_Arboles_Regresion_y_Poda_Cost_Complexity

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Árboles de Regresión y Poda Cost-Complexity
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 09
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/02_Arboles_Regresion_y_Poda_Cost_Complexity.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. Árboles de Decisión para Regresión (`DecisionTreeRegressor`) 📈

Cuando la variable objetivo es continua ($y \in \mathbb{R}$), el árbol divide el espacio en $J$ regiones discretas $R_1, R_2, \dots, R_J$ y predice para cualquier observación en la región $R_j$ el **promedio muestral**:

$$\hat{y}_{R_j} = rac{1}{N_j} \sum_{i \in R_j} y_i$$

El criterio de división busca minimizar la **Suma Residual de Cuadrados (RSS / MSE)**:

$$\text{MSE}(R) = rac{1}{N} \sum_{i=1}^N (y_i - \hat{y})^2$$

<div align="center">
  <table style="border:none; background:transparent;">
    <tr style="border:none;">
      <td style="border:none; text-align:center; padding:10px;">
        <img src="images/dep_predictors.png" width="340" alt="Regresion por tramos" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.85em; color:#64748b;"><b>Aproximación por Funciones Escalonadas</b></p>
      </td>
      <td style="border:none; text-align:center; padding:10px;">
        <img src="images/fitting.png" width="340" alt="Sobreajuste" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.85em; color:#64748b;"><b>Sobreajuste en Árboles sin Restricción</b></p>
      </td>
    </tr>
  </table>
</div>

---
### 2. La Trampa del Sobreajuste y la Poda por Complejidad de Costo (*Cost-Complexity Pruning*) ✂️

Si no se detiene la profundidad del árbol, este crecerá hasta que cada hoja contenga una sola muestra:
* **Entrenamiento:** Exactitud = $100\%$ / MSE = 0.
* **Prueba:** Alta varianza y pésima generalización.

Para regularizar el modelo, se formula la **Poda por Complejidad de Costo Mínimo (*Minimal Cost-Complexity Pruning*)**:

$$R_lpha(T) = R(T) + lpha |T|$$

Donde:
* $R(T)$: Impureza total o error cuadrático de las hojas del subárbol $T$.
* $|T|$: Número total de hojas terminales del subárbol.
* $lpha \ge 0$: Parámetro de penalización por complejidad (`ccp_alpha` en Scikit-Learn).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, urllib.request
import warnings
warnings.filterwarnings('ignore')

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (8.5, 4.5)
plt.rcParams['font.size'] = 10

def load_dataset(filename, module_folder="09 - Decision Trees"):
    local_path = os.path.join(os.getcwd(), "data", filename)
    if os.path.exists(local_path):
        return local_path
    
    parent_path = os.path.join(os.getcwd(), "..", module_folder, "data", filename)
    if os.path.exists(parent_path):
        return parent_path

    raw_url = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/{module_folder.replace(' ', '%20')}/data/{filename}"
    os.makedirs("data", exist_ok=True)
    target_path = os.path.join("data", filename)
    if not os.path.exists(target_path):
        urllib.request.urlretrieve(raw_url, target_path)
    return target_path

print("🚀 Entorno configurado exitosamente para el Módulo 09: Árboles de Decisión.")
```

---
### 3. Ajuste de Árbol de Regresión y Exploración de `ccp_alpha` 🧪

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score

# Cargar dataset de precios inmobiliarios
file_housing = load_dataset('USA_Housing.csv', '07 - Regression')
df_housing = pd.read_csv(file_housing)

features = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']
X = df_housing[features]
y = df_housing['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Árbol no restringido (Overfitting)
tree_overfit = DecisionTreeRegressor(random_state=42)
tree_overfit.fit(X_train, y_train)

print(f"R² en Entrenamiento (Sin restricción): {tree_overfit.score(X_train, y_train):.4f} (¡100%!)")
print(f"R² en Prueba (Sin restricción):        {tree_overfit.score(X_test, y_test):.4f}")
```

```python
# Extracción de la ruta de poda (Cost-Complexity Path)
path = tree_overfit.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

print(f"Número de valores candidatos de alpha generados: {len(ccp_alphas)}")
```

---
##### 🛠️ Práctica 2: Selección del $lpha$ Óptimo con Validación Cruzada

**Objetivo:** Evaluar una grilla de valores de `ccp_alpha` sobre el conjunto de entrenamiento usando validación cruzada y encontrar el árbol podado que maximiza el $R^2$ en generalización.

**Instrucciones:**
1. Selecciona un subconjunto de 15 valores de $lpha$ espaciados uniformemente a lo largo de `ccp_alphas`.
2. Para cada $lpha$, entrena un `DecisionTreeRegressor(ccp_alpha=alpha, random_state=42)`.
3. Calcula el $R^2$ promedio en validación cruzada de 5 pliegues (`cross_val_score(..., cv=5)`).
4. Encuentra el $lpha$ óptimo, ajusta el árbol podado y compara su $R^2$ en el test set frente al árbol sobreajustado.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 2 - Poda Cost-Complexity con Validación Cruzada
# =========================================================================

# 1. Seleccionar alphas candidatos
# sample_alphas = np.linspace(ccp_alphas.min(), ccp_alphas[int(len(ccp_alphas)*0.95)], 15)

# 2. Bucle de evaluación con validación cruzada
# cv_scores = []
# for a in sample_alphas:
#     ...

# 3. Identificar mejor alpha y evaluar en test
# best_a = ...
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
sample_alphas = np.linspace(ccp_alphas.min(), ccp_alphas[int(len(ccp_alphas)*0.9)], 20)
cv_scores = []
test_scores = []

for a in sample_alphas:
    model_pruned = DecisionTreeRegressor(ccp_alpha=a, random_state=42)
    scores = cross_val_score(model_pruned, X_train, y_train, cv=5, scoring='r2', n_jobs=-1)
    cv_scores.append(scores.mean())
    
    model_pruned.fit(X_train, y_train)
    test_scores.append(model_pruned.score(X_test, y_test))

# 1. Identificar el mejor alpha
best_idx = np.argmax(cv_scores)
best_alpha = sample_alphas[best_idx]

# 2. Visualización de la curva de poda
plt.figure(figsize=(9, 4.5))
plt.plot(sample_alphas, cv_scores, marker='o', label='R² Validación Cruzada (CV=5)', color='#0284c7', lw=2.2)
plt.plot(sample_alphas, test_scores, marker='s', label='R² Conjunto de Prueba (Test)', color='#10b981', linestyle='--')
plt.axvline(best_alpha, color='#dc2626', linestyle=':', label=f'Alpha Óptimo ({best_alpha:.2e})')
plt.title('Selección del Parámetro de Poda Alpha (Cost-Complexity Pruning)', fontweight='bold')
plt.xlabel('Parámetro de Complejidad de Costo (ccp_alpha)')
plt.ylabel('Coeficiente de Determinación (R²)')
plt.legend()
plt.show()

# 3. Comparación de resultados
best_tree = DecisionTreeRegressor(ccp_alpha=best_alpha, random_state=42)
best_tree.fit(X_train, y_train)

print("=" * 65)
print("🏆 RESULTADOS COMPARATIVOS: ÁRBOL COMPLETO vs ÁRBOL PODADO")
print("=" * 65)
print(f"• Hojas del Árbol Original:  {tree_overfit.get_n_leaves()} hojas ──► R² Test: {tree_overfit.score(X_test, y_test):.4f}")
print(f"• Hojas del Árbol Podado:    {best_tree.get_n_leaves()} hojas  ──► R² Test: {best_tree.score(X_test, y_test):.4f}")
print("=" * 65)
```
</details>

---
### 4. Resumen y Conclusiones del Cuaderno 02 📌

1. **Árboles de Regresión:** Estiman funciones escalonadas calculando el promedio muestral de cada región ortogonal.
2. **Peligro de Sobreajuste:** Los árboles no restringidos memorizan el ruido muestral con exactitud aparente del 100%.
3. **Poda Cost-Complexity:** Balancea formalmente el error de ajuste contra la cantidad de hojas mediante el parámetro de regularización $lpha$.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
