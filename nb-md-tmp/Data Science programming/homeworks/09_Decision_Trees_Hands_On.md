# 09_Decision_Trees_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Árboles de Decisión y Métodos de Ensamble (Hands-On Lab)
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
        Taller Práctico • Módulo 09
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/09_Decision_Trees_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Instrucciones y Objetivos del Taller Evaluativo

El presente taller evalúa la comprensión teórico-práctica de los **Modelos Basados en Árboles** y los **Métodos de Ensamble (Bagging, Random Forests y Gradient Boosting)** utilizando el conjunto de datos real de detección de spam (`spam.csv`).

El taller se divide en **5 Partes Evaluativas**:
1. **Parte 1: Carga, Estructuración y Partición Estratificada del Dataset.**
2. **Parte 2: Árbol de Decisión Simple y Selección de Profundidad Máxima con Validación Cruzada.**
3. **Parte 3: Poda por Complejidad de Costo Mínimo (*Minimal Cost-Complexity Pruning / ccp_alpha*).**
4. **Parte 4: Random Forest, Importancia de Características y Estimación Out-of-Bag (OOB).**
5. **Parte 5: Gradient Boosting con Optimización de Hiperparámetros y Benchmark Comparativo.**

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

print("🚀 Entorno configurado exitosamente para el Taller 09.")
```

---
### 📌 Parte 1: Carga y Partición Estratificada del Dataset de Spam (1.0 Puntos)

**Instrucciones:**
1. Utiliza `load_dataset('spam.csv', '09 - Decision Trees')` para cargar los datos en un DataFrame de pandas sin encabezado (`header=None`).
2. Asigna nombres a las 57 características predictoras (`Feature_1, Feature_2, ..., Feature_57`) y nombra la última columna como `Spam`.
3. Separa las variables predictoras $X$ y el vector objetivo $y$.
4. Realiza una partición de 70% para entrenamiento y 30% para prueba con `train_test_split`, estratificando por la variable objetivo (`stratify=y`) y fijando `random_state=42`.

```python
# =========================================================================
# TU SOLUCIÓN: Parte 1 - Carga y Partición
# =========================================================================

# 1. Cargar y nombrar columnas
# file_spam = load_dataset('spam.csv', '09 - Decision Trees')
# ...

# 2. Separar X e y
# ...

# 3. train_test_split
# ...
```

---
### 📌 Parte 2: Árbol Simple y Búsqueda de Profundidad Óptima con CV (1.0 Puntos)

**Instrucciones:**
1. Itera sobre un rango de profundidades máximas `max_depth` desde 3 hasta 25 con saltos de 2 (`range(3, 26, 2)`).
2. Para cada profundidad, evalúa un `DecisionTreeClassifier(max_depth=d, random_state=42)` mediante validación cruzada de 5 pliegues (`cross_val_score(..., cv=5, scoring='accuracy')`).
3. Almacena y grafica la media del accuracy para cada profundidad.
4. Identifica la profundidad óptima `best_depth` y reporta la exactitud obtenida en el conjunto de prueba ($X_{test}, y_{test}$).

```python
# =========================================================================
# TU SOLUCIÓN: Parte 2 - Selección de Profundidad
# =========================================================================

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import cross_val_score

# depths = range(3, 26, 2)
# ...
```

---
### 📌 Parte 3: Poda por Complejidad de Costo (*Cost-Complexity Pruning*) (1.0 Puntos)

**Instrucciones:**
1. Entrena un árbol de decisión sin restricciones de profundidad sobre el conjunto de entrenamiento.
2. Extrae la ruta de poda mediante `cost_complexity_pruning_path(X_train, y_train)`.
3. Selecciona una muestra de 15 valores de $lpha$ y evalúa su $F_1\text{-score}$ medio en validación cruzada de 5 pliegues.
4. Entrena el árbol con el $lpha$ óptimo y compara el número de hojas terminales (`best_tree.get_n_leaves()`) y el $F_1\text{-score}$ en prueba frente al árbol no restringido.

```python
# =========================================================================
# TU SOLUCIÓN: Parte 3 - Poda Cost-Complexity
# =========================================================================

# path = ...
# ...
```

---
### 📌 Parte 4: Random Forest, Importancia de Variables y Error OOB (1.0 Puntos)

**Instrucciones:**
1. Entrena un `RandomForestClassifier(n_estimators=150, max_features='sqrt', oob_score=True, random_state=42, n_jobs=-1)` sobre $X_{train}, y_{train}$.
2. Reporta la puntuación Out-of-Bag (`rf_model.oob_score_`) y la exactitud en el conjunto de prueba.
3. Extrae las 10 características con mayor valor en `feature_importances_` y genera un gráfico de barras horizontal ordenado.

```python
# =========================================================================
# TU SOLUCIÓN: Parte 4 - Random Forest y Feature Importance
# =========================================================================

# from sklearn.ensemble import RandomForestClassifier

# ...
```

---
### 📌 Parte 5: Gradient Boosting y Tabla de Benchmark Final (1.0 Puntos)

**Instrucciones:**
1. Entrena un `GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)` sobre $X_{train}, y_{train}$.
2. Calcula para todos los modelos desarrollados (Árbol Simple, Árbol Podado, Random Forest y Gradient Boosting) las métricas:
   * **Exactitud (*Accuracy*)** en Test Set.
   * **$F_1$-Score**.
   * **Área Bajo la Curva ROC (ROC-AUC)**.
3. Consolida los resultados en un `pd.DataFrame` resumen y redacta una breve conclusión técnica justificando cuál es el modelo más adecuado para producción.

```python
# =========================================================================
# TU SOLUCIÓN: Parte 5 - Gradient Boosting y Benchmark
# =========================================================================

# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.metrics import roc_auc_score, f1_score

# ...
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Laboratorio de Machine Learning</i>
  </p>
</div>
