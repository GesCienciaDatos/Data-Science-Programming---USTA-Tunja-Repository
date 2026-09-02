# 04_Boosting_y_Casos_Estudio_Desbalanceados

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Boosting y Modelado en Datos Desbalanceados
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/04_Boosting_y_Casos_Estudio_Desbalanceados.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. El Paradigma de Boosting: Aprender Secuencialmente de los Errores 🎯

A diferencia de Bagging (donde los árboles se entrenan de forma independiente y paralela), **Boosting entrena árboles de forma secuencial**:
1. Cada árbol nuevo se enfoca con **mayor peso en los ejemplos que los árboles anteriores clasificaron incorrectamente**.
2. Los modelos base son típicamente *árboles débiles (*Weak Learners*)* con profundidad muy baja (`max_depth = 1` a `3`, denominados *Stumps*).
3. Convierte un ensamble de modelos débiles en un **predictor de alta precisión con bajo sesgo y baja varianza**.

<div align="center">
  <table style="border:none; background:transparent;">
    <tr style="border:none;">
      <td style="border:none; text-align:center; padding:8px;">
        <img src="images/boosting.png" width="320" alt="Boosting Secuencial" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.8em; color:#64748b;"><b>Ponderación Adaptativa de Errores</b></p>
      </td>
      <td style="border:none; text-align:center; padding:8px;">
        <img src="images/gradient_boosting1.png" width="320" alt="Gradient Descent en Espacio de Funciones" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.8em; color:#64748b;"><b>Gradient Boosting: Ajuste sobre Residuos</b></p>
      </td>
    </tr>
  </table>
</div>

---
### 2. Algoritmos Principales de Boosting:
* **AdaBoost (*Adaptive Boosting*):** Ajusta los pesos de las observaciones en cada iteración aumentando la probabilidad de remuestrear los errores.
* **Gradient Boosting (`GradientBoostingClassifier`):** Formula el aprendizaje como un descenso de gradiente en el espacio de funciones, donde cada nuevo árbol predice los **residuos de pseudo-gradiente** de la función de pérdida.
* **XGBoost / LightGBM / CatBoost:** Implementaciones optimizadas de alto rendimiento con regularización $L_1/L_2$, manejo de valores faltantes y paralelización nativa.

<div align="center">
  <img src="images/kaggle.png" width="500" alt="Dominio en Competiciones" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.12); margin: 10px 0;"/>
  <p style="font-size:0.85em; color:#64748b;"><i>Figura: Los modelos de Gradient Boosting son el estándar de la industria para datos tabulares estructurados.</i></p>
</div>

---
### 3. Manejo de Clases Desbalanceadas (*Class-Imbalance*) ⚖️

Cuando una clase es minoritaria (ej. detección de fraudes o diagnósticos raros), los árboles tienden a ignorarla para maximizar la pureza global.

**Soluciones Integradas en Scikit-Learn:**
1. **`class_weight='balanced'`:** Ajusta los pesos de impureza de las clases de forma inversamente proporcional a sus frecuencias:
   $$w_k = rac{N}{K \cdot N_k}$$
2. **`sample_weight`:** Asigna un vector de pesos individuales para cada observación en el método `.fit(X, y, sample_weight=w)`.

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
### 4. Benchmark Integral: Comparativa de Clasificadores sobre el Dataset de Spam 🧪

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score

# 1. Carga de datos de spam
file_spam = load_dataset('spam.csv', '09 - Decision Trees')
df_spam = pd.read_csv(file_spam, header=None)
X = df_spam.iloc[:, :-1]
y = df_spam.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

# 2. Definición del catálogo de modelos
modelos = {
    "1. Árbol de Decisión Simple": DecisionTreeClassifier(max_depth=8, random_state=42),
    "2. Bagging (100 Árboles)": BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=100, random_state=42, n_jobs=-1),
    "3. Random Forest (100 Árboles)": RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42, n_jobs=-1),
    "4. AdaBoost (100 Estimadores)": AdaBoostClassifier(n_estimators=100, learning_rate=0.8, random_state=42),
    "5. Gradient Boosting (100 Estimadores)": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
}

resultados = []
for nombre, clf in modelos.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    
    resultados.append({
        "Modelo": nombre,
        "Exactitud (Accuracy)": f"{acc*100:.2f}%",
        "F1-Score": f"{f1:.4f}",
        "ROC-AUC": f"{auc:.4f}"
    })

df_res = pd.DataFrame(resultados)
print("=" * 70)
print("🏆 TABLA COMPARATIVA DE RENDIMIENTO (DATASET DE SPAM):")
print("=" * 70)
display(df_res)
```

---
##### 🛠️ Práctica 4: Gran Desafío Integrador — Optimización de Hiperparámetros de Gradient Boosting

**Objetivo:** Diseñar y optimizar un `GradientBoostingClassifier` sobre el dataset de spam utilizando `GridSearchCV` para encontrar la tasa de aprendizaje (`learning_rate`), profundidad (`max_depth`) y número de estimadores óptimos, evaluando la matriz de confusión resultante.

**Instrucciones:**
1. Define una grilla de parámetros:
   ```python
   param_grid = {
       'n_estimators': [50, 100],
       'learning_rate': [0.05, 0.1, 0.2],
       'max_depth': [3, 4]
   }
   ```
2. Ejecuta `GridSearchCV(GradientBoostingClassifier(random_state=42), param_grid, cv=3, scoring='roc_auc', n_jobs=-1)`.
3. Extrae los mejores parámetros y evalúa el clasificador final en el test set.
4. Grafica la Matriz de Confusión normalizada.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 4 - Optimización de Gradient Boosting
# =========================================================================

# 1. Configurar GridSearchCV
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# grid = GridSearchCV(...)
# grid.fit(...)

# 2. Mejor modelo y evaluación
# best_gb = grid.best_estimator_
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. Definir grilla de búsqueda
param_grid = {
    'n_estimators': [50, 100],
    'learning_rate': [0.05, 0.1, 0.2],
    'max_depth': [3, 4]
}

gb_base = GradientBoostingClassifier(random_state=42)
grid_gb = GridSearchCV(gb_base, param_grid, cv=3, scoring='roc_auc', n_jobs=-1)
grid_gb.fit(X_train, y_train)

best_gb = grid_gb.best_estimator_
y_pred_gb = best_gb.predict(X_test)
y_proba_gb = best_gb.predict_proba(X_test)[:, 1]

print("=" * 65)
print(f"✨ MEJORES HIPERPARÁMETROS: {grid_gb.best_params_}")
print(f"• Exactitud Test: {accuracy_score(y_test, y_pred_gb)*100:.2f}%")
print(f"• ROC-AUC Test:   {roc_auc_score(y_test, y_proba_gb):.4f}")
print("=" * 65)

# 2. Matriz de Confusión
cm = confusion_matrix(y_test, y_pred_gb)
plt.figure(figsize=(6, 5), dpi=110)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No-Spam (0)', 'Spam (1)'])
disp.plot(cmap='Blues', values_format='d')
plt.title('Matriz de Confusión - Gradient Boosting Optimizado', fontweight='bold')
plt.grid(False)
plt.show()
```
</details>

---
### 5. Resumen y Conclusiones del Cuaderno 04 y del Módulo 09 📌

1. **Bagging vs Boosting:** Bagging entrena árboles profundos en paralelo para reducir varianza; Boosting entrena árboles superficiales secuencialmente para reducir sesgo.
2. **Dominio en Datos Estructurados:** Gradient Boosting (y frameworks como XGBoost/LightGBM) son los líderes en rendimiento para analítica predictiva tabular.
3. **Manejo de Desbalance:** La ponderación `class_weight='balanced'` permite a los árboles penalizar con mayor severidad los errores en clases minoritarias.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
